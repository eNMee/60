import os.path
from os import path


def load_menu():

    menu_list = []
    if path.exists("menu.txt"):
        with open("menu.txt", "r") as menu:
            menu_list = [menu.split(",") for menu in menu.readlines()]
        for dish in menu_list:
            dish[3] = dish[3].strip("\n")

    return menu_list


