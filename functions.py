import backend as db


def validate_user(username, password):
    '''Takes in a username and password for validation'''
    if username.lower() == "bitvivaz" and password == "123":
        return True
    else:
        return False


def list_commands():
    '''List commands that are available'''
    print('''
    a  - Add Credential
    d  - Delete Credential
    s  - Show All Credentials
    se - Search Credentials
    h  - List Commmands
    e  - Exit
    ''')


def add_credential():
    '''Add credential to database'''
    while True:
        name = input("Name: ")
        if not db.check_existance(name):
            username = input("Username: ")
            password = input("Password: ")
            db.add_credential(name, username, password)
            break
        else:
            print(f"{name} already exists, please try again")


def show_credentials():
    '''Show all credentials in database'''
    print("Name    Username    Password")
    for row in db.show_credentials():
        print(f"{row['name']} {row['username']} {row['password']}")


def search_credentials():
    '''Search all credentials that match in database'''
    name = input("Name: ")
    print("Name    Username    Password")
    for row in db.search_credentials(name):
        print(f"{row['name']} {row['username']} {row['password']}")


def delete_credential():
    '''Delete credential from database'''
    while True:
        name = input("Name: ")
        if db.check_existance(name):
            confirmation = input(
                f"Are you sure you want to delete {name} (Y/N): ")
            if confirmation.lower() == 'y':
                db.delete_credential(name)
                break
            elif confirmation.lower() == 'n':
                print(f"{name} was not deleted")
                break
            else:
                print("Wrong input, please try again")
        else:
            print(f"{name} do not exists, please try again!")
