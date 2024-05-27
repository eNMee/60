def check_user(login,password,users_list,reg = False):
    if not reg:
        for user in users_list:
            if user[0] == login and user[1] == password:
                cond = user[3]
                if cond.rstrip("\n") == "admin" or cond == "admin":
                    current_user = "admin"
                    wallet = user[2]
                    return current_user, wallet
                elif cond.rstrip("\n") == "user" or cond == "user":
                    current_user = "user"
                    wallet = user[2]
                    return current_user, wallet

    if reg:
        for user in users_list:
            if user[0] == login and user[1] == password:
                reg = None
                return "User already exists!"
            elif user[0] == login:
                return "Login already exists!"
            else:
                u1 = login, password, "0", "user"
                users_list.append(u1)
                new_info = []
                for u in users_list:
                    string_line = ""
                    for word in range(0,len(u)):
                        if word == len(u) - 1:
                            string_line += u[word]
                        else:
                            string_line += u[word] + ","
                    new_info.append(string_line)
                with open("users.txt", "w") as f:
                    f.writelines(new_info)
                    return "Successeful reg!"






