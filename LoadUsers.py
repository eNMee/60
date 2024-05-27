
import os.path
from os import path


def load_users():

    users_list = []
    if path.exists("users.txt"):
        with open("users.txt", "r") as users:
            users_list = [user.split(",") for user in users.readlines()]
            for user in users_list:
                user[3] = user[3].strip("\n")
    return users_list
