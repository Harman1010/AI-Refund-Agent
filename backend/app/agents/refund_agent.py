from app.tools.customer_tool import get_customer
from app.tools.order_tool import get_order
from app.tools.policy_tool import check_policy
from app.llm import generate_reply


def extract_order_id(message):

    words = message.split()

    for word in words:
        if word.startswith("O"):
            return word

    return None


def process_refund(message):

    logs = []

    order_id = extract_order_id(message)

    if not order_id:
        return {
            "reply": "Please provide your order ID.",
            "logs": ["Order ID not found"]
        }

    logs.append(f"Order ID found: {order_id}")

    customer = get_customer(order_id)

    if not customer:
        logs.append("Customer lookup failed")

        return {
            "reply": "Customer not found.",
            "logs": logs
        }

    logs.append("Customer found")

    order = get_order(order_id)

    if not order:
        logs.append("Order lookup failed")

        return {
            "reply": "Order not found.",
            "logs": logs
        }

    logs.append("Order found")

    approved, reason = check_policy(order)

    logs.append("Policy checked")
    logs.append(reason)

    if approved:

        logs.append("Refund approved")

        reply = generate_reply(
            reason,
            True,
            order_id
        )

        return {
            "reply": reply,
            "logs": logs
        }

    logs.append("Refund denied")

    reply = generate_reply(
        reason,
        False,
        order_id
    )

    return {
        "reply": reply,
        "logs": logs
    }