from LoadOrders import load_all_users_order
from UpdateOrders import add_order


def pay(login,cart,wallet,order_list):
    total = 0
    meals = []
    for val in cart:
        total += int(val[1])
        meals.append(val[0])

    if total <= int(wallet):
        wallet = int(wallet) - total
        order = [login, "active", str(total),]
        for meal in meals:
            order.append(meal)
        print("Оплата прошла!")
        add_order(order)
        cart = []
        return cart,wallet
    else:
        print("Недостатньо коштів на рахунку!")
        return order_list
