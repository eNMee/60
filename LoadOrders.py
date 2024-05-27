import os.path
from os import path


def load_user_orders(login):
    if path.exists("orders.txt"):
        with open("orders.txt", "r") as orders:
            order_list = [order.split(",") for order in orders.readlines()]
        user_order_list = []
        for order in order_list:
            if order[0] == login:
                user_order_list.append(order)

        return user_order_list


def load_all_users_order():
    if path.exists("orders.txt"):
        with open("orders.txt", "r") as orders:
            all_orders = [order.split(",") for order in orders.readlines()]
        for order in all_orders:
            if len(order)-1:
                order[len(order)-1] = order[len(order)-1].strip("\n")
        return all_orders


