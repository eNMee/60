from ClassCart import Cart


def edit_cart(cart):
    try:
        new_cart = cart
        while new_cart:
            Cart.show_cart(new_cart)
            delete_meal = input("Введіть назву страви яку ви хочете видалити(exit щоб вийти): ")

            if delete_meal != "exit":
                for val in range(0,len(new_cart)-1):
                    for info in new_cart[val]:
                        if delete_meal == info:
                            new_cart.pop(val)

            elif delete_meal == "exit":
                    if len(cart) == len(new_cart):
                        return cart
                    elif new_cart:
                        return new_cart
                    elif not new_cart:
                        print("Корзина порожня!")
                        return
    except KeyboardInterrupt as e:
        print("Error: " + str(e))
    except FileNotFoundError as e:
        print("FileError:"+ str(e))
    except Exception as e:
        print("Exception: " + str(e))