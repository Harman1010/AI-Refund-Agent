import json


def get_customer(order_id):

    with open("app/data/customers.json", "r") as file:
        customers = json.load(file)

    for customer in customers:
        if order_id in customer["orders"]:
            return customer

    return None