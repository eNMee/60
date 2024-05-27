def edit_menu(menu_list):
    try:
        while True:
            e_menu = input("Введіть назву страви яку ви хочете змінити(exit щоб вийти): ")

            if e_menu != "exit":
                choice_change = input("1.Змінити назву.\n"
                                      "2.Змінити вагу.\n"
                                      "3.Змінити ціну.\n"
                                      "4.Змінити категорії(dish or drink) .\n"
                                      "5.Вихід"
                                      "Введіть ваш вибір:")
                if choice_change == "1":
                    new_name = input("Введіть нову назву: ")
                    for meal in menu_list:
                        if meal[0] == e_menu:
                            meal[0] = new_name
                elif choice_change == "2":
                    new_weight = input("Введіть нову вагу:")
                    for meal in menu_list:
                        if meal[0] == e_menu:
                            meal[1] = new_weight
                elif choice_change == "3":
                    new_price = input("Введіть нову ціну:")
                    for meal in menu_list:
                        if meal[0] == e_menu:
                            meal[2] = new_price
                elif choice_change == "4":
                    new_type = input("Введіть нову категорію(drink or dish):")
                    for meal in menu_list:
                        if meal[0] == e_menu:
                            meal[3] = new_type
                elif choice_change == "5":
                    pass

            elif e_menu == "exit":
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
                print("Успішно відредаговано!")
                return print("Успішно відредаговано!")
    except KeyboardInterrupt as e:
        print("Error: " + str(e))
    except FileNotFoundError as e:
        print("FileError:"+ str(e))
    except Exception as e:
        print("Exception: " + str(e))


