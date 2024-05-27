def update_menu(menu_list):
    new_line = []
    name = input("Enter name of meal or drink:")
    new_line.append(name)
    weight = input("Вага або об'єм:")
    new_line.append(weight)
    price = input("Введіть ціну:")
    new_line.append(price)
    type = input("Введіть категорію(drink or dish):")
    new_line.append(type)
    menu_list.append(new_line)
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