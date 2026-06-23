import json


def get_order(order_id):

    with open("app/data/orders.json", "r") as file:
        orders = json.load(file)

    for order in orders:
        if order["order_id"] == order_id:
            return order

    return None