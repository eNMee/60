from LoadOrders import load_all_users_order


def add_order(order):
    try:
        old_list = load_all_users_order()
        old_list.append(order)
        new_list = []
        for o in old_list:
            string_line = ""
            for info in range(0, len(o)):
                if info == len(o) - 1:
                    string_line += o[info]+"\n"
                else:
                    string_line += o[info] + ","
            new_list.append(string_line)

        with open("orders.txt", "w") as f:
            f.writelines(new_list)
    except KeyboardInterrupt as e:
        print("Error: " + str(e))
    except FileNotFoundError as e:
        print("FileError:"+ str(e))
    except Exception as e:
        print("Exception: " + str(e))

