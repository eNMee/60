import shutil
import unittest
import os.path
from os import path


class TestingModuls(unittest.TestCase):

    def test_change_order(self):
        all_orders = [["nazar","active","80","cola"]]
        login = "nazar"      #input("Введіть логін замовника(exit щоб вийти): ")
        if login == "exit":
            return
        else:
            new_status = "inactive"     #input("Введіть новий статус: ")
            for order in all_orders:
                if order[0] == login and order[1] != "inactiv":
                    order[1] = new_status
            self.assertEqual([["nazar","inactive","80","cola"]],all_orders)

    def test_load_user_orders(self):
        login = "nazar"
        order_list = [["nazar","active","150","pizza"],["sasha","active","100","tea"]]
        user_order_list = []
        for order in order_list:
            if order[0] == login:
                user_order_list.append(order)

        self.assertEqual([["nazar","active","150","pizza"]],user_order_list)

    def test_load_all_users_order(self):
        all_orders = [["nazar","active","150","pizza"],["sasha","active","100","tea"]]
        for order in all_orders:
            if len(order) - 1:
                order[len(order) - 1] = order[len(order) - 1].strip("\n")
        self.assertEqual([["nazar","active","150","pizza"],["sasha","active","100","tea"]],all_orders)

    def test_delete_menu(self):
        menu_list = [["tea","200","50","drink"],["cola","250","30","drink"]]
        while True:
            del_menu = "tea"   #input("Введіть назву страви яку ви хочете видалити(exit щоб вийти):")
            counter = 0
            for meal in menu_list:
                if meal[0] == del_menu:
                    menu_list.pop(counter)
            counter += 1
            break

        self.assertEqual([['cola', '250', '30', 'drink']],menu_list)

    def test_edit_menu(self):
        menu_list = [["tea", "200", "50", "drink"], ["cola", "250", "30", "drink"]]
        while True:
            e_menu ="tea"#input("Введіть назву страви яку ви хочете змінити(exit щоб вийти): ")

            while e_menu:
                choice_change = "1"#input("1.Змінити назву.\n"
                                          # "2.Змінити вагу.\n"
                                          # "3.Змінити ціну.\n"
                                          # "4.Змінити категорії(dish or drink) .\n"
                                          # "5.Вихід"
                                          # "Введіть ваш вибір:")
                if choice_change == "1":
                    new_name = "coffee" #input("Введіть нову назву: ")
                    for meal in menu_list:
                        if meal[0] == e_menu:
                            meal[0] = new_name
                            return menu_list
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
                self.assertEqual(menu_list,[["coffee", "200", "50", "drink"], ["cola", "250", "30", "drink"]])

    def test_update_cart(self):
        menu_list = [["tea", "200", "50", "drink"], ["cola", "250", "30", "drink"]]
        new_cart = [["tea","50"]]
        while True:
            dish = "cola"  #input("Напишіть назву страви або напою(exit для виходу):")
            if dish != "exit":
                for d in menu_list:
                    if d[0] == dish:
                        new_cart.append([dish, d[2]])
                        return new_cart

            self.assertEqual([["tea","50"],["cola","30"]],new_cart)

    def test_add_order(self):
        order = ["nazar","active","1000","tea"]
        old_list =[["sasha","inactive","100","cola"]]
        old_list.append(order)
        new_list = []
        for o in old_list:
            string_line = ""
            for info in range(0, len(o)):
                if info == len(o) - 1:
                    string_line += o[info] + "\n"
                else:
                    string_line += o[info] + ","
            new_list.append(string_line)
        self.assertEqual(["sasha,inactive,100,cola\n","nazar,active,1000,tea\n"],new_list)

    def test_update_menu(self):
        menu_list = [["tea", "200", "50", "drink"], ["cola", "250", "30", "drink"]]
        new_line = []
        name = "coffe"#input("Enter name of meal or drink:")
        new_line.append(name)
        weight = "100"#input("Вага або об'єм:")
        new_line.append(weight)
        price = "70"#input("Введіть ціну:")
        new_line.append(price)
        type = "drink"#input("Введіть категорію(drink or dish):")
        new_line.append(type)
        menu_list.append(new_line)

        self.assertEqual([["tea", "200", "50", "drink"], ["cola", "250", "30", "drink"], ["coffe","100","70","drink"]],
                         menu_list)

    def test_save_users(self):
        users_list = [["nazar","123","1000","admin"],["sasha","1234","100","user"]]
        new_users_list = []
        for user in users_list:
            string_line = ""
            for word in range(0, len(user)):
                if word == len(user) - 1:
                    string_line += user[word]
                else:
                    string_line += user[word] + ","
            new_users_list.append(string_line)
        self.assertEqual(["nazar,123,1000,admin","sasha,1234,100,user"],new_users_list)

    def test_save_balance(self):
        login = "nazar"
        wallet = "2000"
        users_list = [["nazar", "123", "1000", "admin"], ["sasha", "1234", "100", "user"]]
        for user in users_list:
            if user[0] == login:
                user[2] = wallet

        new_users_list = []
        for o in users_list:
            string_line = ""
            for info in range(0, len(o)):
                if info == len(o) - 1:
                    string_line += o[info]
                else:
                    string_line += str(o[info]) + ","
            new_users_list.append(string_line)
        self.assertEqual(["nazar,123,2000,admin","sasha,1234,100,user"],new_users_list)

    def test_pay(self):#(login, cart, wallet, order_list):
        login = "nazar"
        cart = [["tea","50"]]
        wallet = "2000"
        order_list = []
        total = 0
        meals = []
        for val in cart:
            total += int(val[1])
            meals.append(val[0])

        if total <= int(wallet):
            wallet = int(wallet) - total
            order = [login, "active", str(total), ]
            for meal in meals:
                order.append(meal)
            print("Оплата прошла!")
            order_list.append(order)
            cart = []

            self.assertEqual([["nazar","active","50","tea"]],order_list)

    def test_load_users(self):
        users_list = ["nazar,123,1000,admin","sasha,1234,100,user"]

        users_list = [user.split(",") for user in users_list]
        for user in users_list:
                user[3] = user[3].strip("\n")
        self.assertEqual([["nazar", "123", "1000", "admin"], ["sasha", "1234", "100", "user"]],users_list)

    def test_load_menu(self):
        menu_list = ["tea,200,50,drink","cola,250,30,drink","coffe,100,70,drink"]
        menu_list = [menu.split(",") for menu in menu_list]
        for dish in menu_list:
            dish[3] = dish[3].strip("\n")

        self.assertEqual([["tea", "200", "50", "drink"], ["cola", "250", "30", "drink"], ["coffe","100","70","drink"]],menu_list)

    def test_edit_cart(self):
        cart = [["tea","20"],["cola","30"]]
        new_cart = []
        delete_meal = "cola"# input("Введіть назву страви яку ви хочете видалити(exit щоб вийти): ")
        for val in range(0, len(new_cart) - 1):
            for info in new_cart[val]:
                if delete_meal == info:
                    cart.pop(val)
                    new_cart =cart
                    break
                self.assertEqual([["tea","20"]],new_cart)

    def test_show_all_drinks(self):
        menu_list = [["tea", "200", "50", "drink"], ["cola", "250", "30", "drink"], ["coffe","100","70","dish"]]
        drinks_list = [i for i in menu_list if i[3] == "drink"]

        self.assertEqual([["tea", "200", "50", "drink"], ["cola", "250", "30", "drink"]],drinks_list)

    def test_show_all_dishes(self):
        menu_list = [["tea", "200", "50", "drink"], ["cola", "250", "30", "drink"], ["coffe", "100", "70", "dish"]]
        dishes_list = [i for i in menu_list if i[3] == "dish"]

        self.assertEqual([["coffe", "100", "70", "dish"]], dishes_list)




