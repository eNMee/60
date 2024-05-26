def check_user(login,password,users_list):
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