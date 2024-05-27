def delete_menu(menu_list):
    while True:
        del_menu = input("Введіть назву страви яку ви хочете видалити(exit щоб вийти):")
        counter = 0
        for meal in menu_list:
            if meal[0] == del_menu:
                menu_list.pop(counter)
                new_list = []
                for o in menu_list:
                    string_line = ""
                    for info in range(0, len(o)):
                        if info == len(o) - 1:
                            string_line += o[info] + "\n"
                        else:
                            string_line += o[info] + ","
                    new_list.append(string_line)
                    with open("menu.txt", "w") as f:
                        f.writelines(new_list)
                    break
            counter += 1
