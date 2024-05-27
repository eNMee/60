from LoadOrders import load_all_users_order


def add_order(order):
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

