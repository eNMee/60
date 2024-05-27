class Cart:
    @staticmethod
    def show_cart(cart):
        try:
            if cart:
                prices = []
                print("Cart:\n"
                      "\t Meals\t\tPrice")
                for val in cart:
                    print(f"\t {val[0]}\t\t{val[1]}")
                    prices.append(val[1])
                total = 0
                for price in prices:
                    total += int(price)
                print(f" \t     \t\tTotal\n"
                      f" \t     \t\t{total}")

            elif not cart:
                print("Ваша корзина порожня!")
        except KeyboardInterrupt as e:
            print("Error: " + str(e))
        except FileNotFoundError as e:
            print("FileError:" + str(e))
        except Exception as e:
            print("Exception: " + str(e))
