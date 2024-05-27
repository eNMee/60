import os.path
from os import path


class Menu:
    pass

class ShowMenu:
    def __init__(self,menu_list):
        self.menu_list = menu_list

    @staticmethod
    def show_menu_list(menu_list):
        try:
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
        except KeyboardInterrupt as e:
            print("Error: " + str(e))
        except FileNotFoundError as e:
            print("FileError:" + str(e))
        except Exception as e:
            print("Exception: " + str(e))

    @staticmethod
    def show_all_drinks(menu_list):
        try:
            drinks_list = [i for i in menu_list if i[3] == "drink"]

            for val in drinks_list:
                print(f"name:{val[0]}\n"
                      f"weight:{val[1]}\n"
                      f"price:{val[2]}\n"
                      f"type:{val[3]}\n")
        except KeyboardInterrupt as e:
            print("Error: " + str(e))
        except FileNotFoundError as e:
            print("FileError:" + str(e))
        except Exception as e:
            print("Exception: " + str(e))


    @staticmethod
    def show_all_dishes(menu_list):
        try:
            dish_list = [i for i in menu_list if i[3] == "dish"]
            for val in dish_list:
                print(f"name:{val[0]}\n"
                      f"weight:{val[1]}\n"
                      f"price:{val[2]}\n"
                      f"type:{val[3]}\n")
        except KeyboardInterrupt as e:
            print("Error: " + str(e))
        except FileNotFoundError as e:
            print("FileError:" + str(e))
        except Exception as e:
            print("Exception: " + str(e))

    @staticmethod
    def search_dish(menu_list, dish):
        try:
            res = [i for i in menu_list if i[0] == dish]
            for val in res:
                print(f"name:{val[0]}\n"
                      f"weight:{val[1]}\n"
                      f"price:{val[2]}\n"
                      f"type:{val[3]}\n")
        except KeyboardInterrupt as e:
            print("Error: " + str(e))
        except FileNotFoundError as e:
            print("FileError:" + str(e))
        except Exception as e:
            print("Exception: " + str(e))





