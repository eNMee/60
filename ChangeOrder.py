def change_order(all_orders):
    login = input("Введіть логін замовника(exit щоб вийти): ")
    if login == "exit":
        return
    else:
        new_status = input("Введіть новий статус: ")
        for order in all_orders:
            if order[0] == login and order[1] != "inactiv":
                order[1] = new_status

        new_list = []
        for o in all_orders:
            string_line = ""
            for info in range(0, len(o)):
                if info == len(o) - 1:
                    string_line += o[info] + "\n"
                else:
                    string_line += o[info] + ","
            new_list.append(string_line)
            with open("orders.txt", "w") as f:
                f.writelines(new_list)
        print("Статус успішно змінено!")
        return print("Успішно змінено!")





