def check_user(login,password,users_list,reg = False):
    try:
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
            sovpadenie = "0"
            counter = 0
            while sovpadenie == "0" and counter < len(users_list):
                counter = 0
                for user in users_list:
                    if user[0] == login:
                        sovpadenie = "1"
                    counter += 1
            if sovpadenie == "0":
                u1 = login, password, "0", "user"
                users_list.append(u1)
                new_info = []
                for u in users_list:
                    string_line = ""
                    for word in range(0,len(u)):
                        if word == len(u) - 1:
                            string_line += u[word] + "\n"
                        else:
                            string_line += u[word] + ","
                    new_info.append(string_line)

                with open("users.txt", "w") as f:
                    f.writelines(new_info)
                    return "Successeful reg!"

            elif sovpadenie == "1":
                print("User already exists")

    except KeyboardInterrupt as e:
        print("Error: " + str(e))
    except FileNotFoundError as e:
        print("FileError:"+ str(e))
    except Exception as e:
        print("Exception: " + str(e))




