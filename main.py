from functions import list_commands, add_credential, search_credentials
greeted = False


if __name__ == "__main__":
    print("Welcome To Your Password Manager")
    #username = input("Username: ")
    #password = input("Password: ")
    # logged_in = validate_user(username, password)
    logged_in = True
    while logged_in:
        if not greeted:
            #print(f"\nWelcome back {username}!")
            list_commands()
        greeted = True

        command = input("Command: ")

        if command == 'a':
            add_credential()
        elif command == 'e':
            break
        else:
            print("Command not found, please try again")

    else:
        print('failed')
