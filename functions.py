import backend as db
from encryption import encrypted_password, decrypt_password


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
        if not db.check_existance(name) and name != '':
            while True:
                username = input("Username: ")
                if username != '':
                    while True:
                        password = input("Password: ")
                        if password != '':
                            password = encrypted_password(password)
                            db.add_credential(name, username, password)
                            return
                        elif password == '':
                            print("Please insert a valid password")
                elif username == '':
                    print("Please insert a valid username")
        elif name == '':
            print("Please insert a valid name")
        else:
            print(f"{name} already exists, please try again")


def search_credentials():
    '''Search all credentials that match in database'''
    name = input("Name: ")
    print("Name    Username    Password")
    for row in db.search_credentials(name):
        print(
            f"{row['name']} {row['username']} {decrypt_password(row['password'])}")
