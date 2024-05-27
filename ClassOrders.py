from LoadOrders import load_user_orders


class Order:
    @staticmethod
    def show_orders(login,orders_list):
        try:
            res = load_user_orders(login)
            for order in res:
                if order[1] == "active":
                    print("\nOrder:")
                    order_line = "Orders:"
                    for info in range(0,len(order)):
                        if info == 3:
                            order_line += f"{order[info]}"
                        elif info > 3:
                            order_line += f",{order[info]}"
                        elif info == 2:
                            print(f"Price:{order[2]}")
                        elif info == 1:
                            print(f"Status:{order[1]}")
                    print(order_line + "\n")
        except KeyboardInterrupt as e:
            print("Error: " + str(e))
        except FileNotFoundError as e:
            print("FileError:" + str(e))
        except Exception as e:
            print("Exception: " + str(e))



