import os.path
from os import path

class Menu:
    pass


class ShowMenu:
    def __init__(self,menu_list):
        self.menu_list = menu_list

    @staticmethod
    def show_menu_list(self,menu_list):
        dish_list = [i for i in menu_list if i[3] == "dish"]
        drinks_list = [i for i in menu_list if i[3] == "drink"]

        for val in dish_list:
            print(f"name:{val[0]}\n"
                  f"weight:{val[1]}\n"
                  f"price:{val[2]}\n"
                  f"type:{val[3]}\n")

        for val in drinks_list:
            print(f"name:{val[0]}\n"
                  f"weight:{val[1]}\n"
                  f"price:{val[2]}\n"
                  f"type:{val[3]}\n")

    @staticmethod
    def show_all_drinks(self, menu_list):
        drinks_list = [i for i in menu_list if i[3] == "drink"]

        for val in drinks_list:
            print(f"name:{val[0]}\n"
                  f"weight:{val[1]}\n"
                  f"price:{val[2]}\n"
                  f"type:{val[3]}\n")


    @staticmethod
    def show_all_dishes(menu_list):
        dish_list = [i for i in menu_list if i[3] == "dish"]
        for val in dish_list:
            print(f"name:{val[0]}\n"
                  f"weight:{val[1]}\n"
                  f"price:{val[2]}\n"
                  f"type:{val[3]}\n")

    @staticmethod
    def search_dish(menu_list, dish):
        res = [i for i in menu_list if i[0] == dish]
        for val in res:
            print(f"name:{val[0]}\n"
                  f"weight:{val[1]}\n"
                  f"price:{val[2]}\n"
                  f"type:{val[3]}\n")





