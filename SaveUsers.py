def save_users(users_list):
    try:
        new_users_list = []
        for user in users_list:
            string_line = ""
            for word in range(0, len(user)):
                if word == len(user) - 1:
                    string_line += user[word]
                else:
                    string_line += user[word] + ","
            new_users_list.append(string_line)
        with open("users.txt", "w") as f:
            f.writelines(new_users_list)
    except KeyboardInterrupt as e:
        print("Error: " + str(e))
    except FileNotFoundError as e:
        print("FileError:"+ str(e))
    except Exception as e:
        print("Exception: " + str(e))

