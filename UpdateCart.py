from ClassMenu import ShowMenu
from LoadMenu import load_menu


def update_cart(cart, menu_list):
    ShowMenu.show_menu_list(menu_list)
    new_cart = cart
    while True:
        dish = input("Напишіть назву страви або напою(exit для виходу):")
        if dish != "exit":
            for d in menu_list:
                if d[0] == dish:
                    new_cart.append([dish, d[2]])

        if dish == "exit":
            if not new_cart:
                return cart
            elif new_cart:
                return new_cart
