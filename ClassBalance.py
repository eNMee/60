import os.path
from os import path

class Balance:
    def __init__(self, login, users_list):
        self.login = login
        self.users_list = users_list

    @staticmethod
    def show_balance(login,users_list):
        try:
            for user in users_list:
                if user[0] == login:
                    print(f"Ваш баланс:{user[2]}")
        except Exception as e:
            print("Error: "+ str(e))

    @staticmethod
    def update_balance(login,users_list):
        try:
            update = input("Введіть на яку сумму ви хочете поповнити баланс:")
            balance = 0
            for user in users_list:
                if user[0] == login:
                    current_balance = user[2]
                    balance = int(current_balance) + int(update)
                    user[2] = str(balance)
            print(f"Ви успішно поповнили баланс на {update}\n"
                  f"Загальний баланс {balance}")
            return users_list,balance
        except KeyboardInterrupt as e:
            print("Error: " + str(e))
        except FileNotFoundError as e:
            print("FileError:" + str(e))
        except Exception as e:
            print("Exception: " + str(e))

    @staticmethod
    def balance_after_pay(login,balance,users_list):
        try:
            for user in users_list:
                if user[0] == login:
                    user[2] = str(balance)
            return users_list
        except Exception as e:
            print("Error: "+ str(e))
