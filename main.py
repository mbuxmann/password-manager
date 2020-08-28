credentials = dict()
greeted = False


def validate_user(username, password):
    if username.lower() == "bitvivaz" and password == "123":
        return True
    else:
        return False


def list_commands():
    print('''
    a - Add Credentials
    d - Delete Credentials
    s - Search Credentials
    4 - Show All Credentials
    h - List Commmands
    e - Exit
    ''')


def add_credentials():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    credentials[website] = {'Username': username, 'Password': password}
    print(f'{website}: {username} {password} added')


def show_credentials():
    for credential in credentials:
        print(
            f"{credential} {credential['Username']} {credential['Password']}")


def delete_credentials():
    website = input("Website: ")


if __name__ == "__main__":
    print("Welcome To Your Password Manager")
    username = input("Username: ")
    password = input("Password: ")
    # logged_in = validate_user(username, password)
    logged_in = True
    while logged_in:
        if not greeted:
            print(f"\nWelcome back {username}!")
            list_commands()
        greeted = True

        command = input("Command: ")

        if command == 'a':
            add_credentials()
        elif command == 's':
            show_credentials()
        elif command == 'd':
            delete_credentials()
        elif command == 'h':
            list_commands()
        elif command == 'e':
            break
        else:
            print("Command not found, please try again")

    else:
        print('failed')
