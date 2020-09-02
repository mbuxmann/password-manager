import tkinter as tk
import tkinter.ttk as ttk
from encryption import encrypted_password, decrypt_password
import backend as db


def get_credentials(tree):
    '''Retrieves all credentials from the database and inserts it into the tree widget'''
    for row in db.show_credentials():
        tree.insert("", 'end', text=row['name'], values=(
            row['username'], decrypt_password(row['password'])))


class MainframeApp:
    def __init__(self, master=None):
        # build ui
        frame_main = ttk.Frame(master)
        frame_main.config(height='600', width='600')
        frame_main.grid()

        # Creates tree widget
        tree = ttk.Treeview(frame_main)

        tree["columns"] = ("one", "two")

        tree.column("#0")
        tree.column("one")
        tree.column("two")

        tree.heading("#0", text="Website")
        tree.heading("one", text="Username")
        tree.heading("two", text="Password")

        tree.grid(padx='5', pady='5', rowspan='20')

        get_credentials(tree)

        tree.bind("<<TreeviewSelect>>", self.select, "+")

        button_add = ttk.Button(frame_main)
        button_add.config(text='Add')
        button_add.grid(column='1', padx='5', row='0')
        button_delete = ttk.Button(frame_main)
        button_delete.config(text='Delete')
        button_delete.grid(column='1', padx='5', row='1')
        button_logout = ttk.Button(frame_main)
        button_logout.config(text='Logout')
        button_logout.grid(column='1', padx='5', row='2')

        # Main widget
        self.mainwindow = frame_main

    def select(self, e):
        print([tree.item(x) for x in tree.selection()])

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Password Manager")
    app = MainframeApp(root)
    app.run()
