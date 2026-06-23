from datetime import datetime


def check_policy(order):

    purchase_date = datetime.strptime(
        order["purchase_date"],
        "%Y-%m-%d"
    )

    days = (datetime.now() - purchase_date).days

    if days > 30:
        return False, "Order is older than 30 days"

    if order["product_type"] == "digital":
        return False, "Digital products are not refundable"

    if not order["delivered"]:
        return False, "Order has not been delivered"

    if order["clearance"]:
        return False, "Clearance items cannot be refunded"

    return True, "Eligible for refund"