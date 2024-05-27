from LoadUsers import load_users


def save_balance(login, wallet):
    users_list = load_users()
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

    with open("users.txt", "w") as f:
        f.writelines(new_users_list)
