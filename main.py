# Завдання 2: Система замовлення їжі онлайн
#
# Опис:
# 	Створіть систему для замовлення їжі онлайн, яка включає у себе керування меню ресторану,
# замовленнями користувачів та обробкою платежів. Система повинна дозволяти користувачам
# переглядати меню, робити замовлення, перевіряти статус свого замовлення та оплачувати онлайн.
#
# Функції:
#
# 	Перегляд меню ресторану з можливістю пошуку за категоріями та стравами.
# Додавання та оновлення страв у меню рестораном.
# Робота з кошиком: додавання страв, видалення страв, оформлення замовлення.
# Обробка платежів (симуляція, без реальних транзакцій).
# Відстеження статусу замовлень користувачем.

# Потрібно створити:
# Модулі для керування меню, замовленнями, користувачами та обробкою платежів.
# Класи для представлення страв, меню, замовлень, користувачів та платежів.
# Винятки для обробки помилок, наприклад, недостатньо коштів для платежу або замовлення недоступної страви.
# Зберігання даних про меню, замовлення та користувачів у файлах.
# Використання Git для керування версіями коду системи.
#
# Тестування:
# 	Написання модульних тестів для перевірки кожної частини системи, включаючи логіку замовлення,
# платежі та управління меню.

import os.path
from os import path

from CheckUser import check_user
from LoadMenu import load_menu
from LoadUsers import load_users
from ClassMenu import ShowMenu
from ClassBalance import Balance
from SaveUsers import save_users


def main():
    users_list = load_users()
    condition = False
    while not condition:
        choice_enter = input("1.Увійти в додаток.\n"
                             "2.Зареєструватися.\n"
                             "3.Вийти.\n"
                             "Введіть ваш вибір:")

        if choice_enter == "1":

            login = input("Уведіть ваш логін:")
            password = input("Уведіть ваш пароль:")
            condition, balance = check_user(login, password,users_list)

            if condition == "admin":
                print("You are admin!")

            elif condition == "user":
                print("Successful enter!\n"
                      f"Welcome,{login}!")
                wallet = balance
                cart = []
                while condition:
                    menu_list = load_menu()
                    choice = input("1.Меню\n"
                                   "2.Статус замовлення\n"
                                   "3.Корзина\n"
                                   "4.Баланс\n"
                                   "5.Вихід\n"
                                   "Введіть ваш вибір:")
                    if choice == "1":
                        choice_menu = input("1.Показати все меню.\n"
                                       "2.Показати напої.\n"
                                       "3.Показати страви.\n"
                                       "4.Пошук за назвою страви\n"
                                       "Введіть ваш вибір:")
                        if choice_menu == "1":
                            ShowMenu.show_menu_list(menu_list)
                        elif choice_menu == "2":
                            ShowMenu.show_all_drinks(menu_list)
                        elif choice_menu == "3":
                            ShowMenu.show_all_dishes(menu_list)
                        elif choice_menu == "4":
                            name = input("Введіть назву страви:")
                            ShowMenu.search_dish(menu_list ,name)
                    elif choice == "2":
                        pass
                    elif choice == "3":
                        pass
                    elif choice == "4":
                        choice_wallet = input("1.Переглянути баланс.\n"
                                              "2.Поповнити баланс.\n"
                                              "3.Вихід\n"
                                              "Введіть ваш вибір:")
                        if choice_wallet == "1":
                            Balance.show_balance(login,users_list)
                        elif choice_wallet == "2":
                            users_list, wallet = Balance.update_balance(login, users_list)
                            save_users(users_list)
                        elif choice_wallet == "3":
                            pass

                    elif choice =="5":
                        pass


            else:
                print("Wrong info or user doesnt exists!\n"
                      "Try again!")

        elif choice_enter == "2":

            login = input("Уведіть ваш логін:")
            password = input("Уведіть ваш пароль:")
            res = check_user(login, password, users_list, reg = True)

            if res == "User already exists!":
                print("User already exists!")

            elif res == "Login already exists!":
                print("Login already exists!")

            elif res == "Successeful reg!":
                users_list = load_users()
                print("GOOD!")

        elif choice_enter == "3":
            print("Good Bye!")
            break







if __name__ == '__main__':
    main()