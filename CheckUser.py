def check_user(login,password,users_list,reg = False):
    if not reg:
        for user in users_list:
            if user[0] == login and user[1] == password:
                cond = user[3]
                if cond.rstrip("\n") == "admin":
                    current_user = "admin"
                    return current_user
                elif cond.rstrip("\n") == "user":
                    current_user = "user"
                    return current_user
            else:
                current_user = False
                return current_user
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






