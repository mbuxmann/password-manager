import tkinter as tk
import tkinter.ttk as ttk
from encryption import encrypted_password, decrypt_password
import backend as db


class MainframeApp:
    def __init__(self, master=None):
        self.selected_credential = None
        # build ui
        frame_main = ttk.Frame(master)
        frame_main.config(height='600', width='600')
        frame_main.grid()

        # Creates tree widget
        self.tree = ttk.Treeview(frame_main)

        self.tree["columns"] = ("one", "two")

        self.tree.column("#0")
        self.tree.column("one")
        self.tree.column("two")

        self.tree.heading("#0", text="Website")
        self.tree.heading("one", text="Username")
        self.tree.heading("two", text="Password")

        self.tree.grid(padx='5', pady='5', rowspan='20')

        self.get_credentials()

        self.tree.bind("<<TreeviewSelect>>", self.select)

        # Create buttons
        button_add = ttk.Button(frame_main)
        button_add.config(text='Add')
        button_add.grid(column='1', padx='5', row='0')
        button_delete = ttk.Button(
            frame_main, command=self.delete_credential)
        button_delete.config(text='Delete')
        button_delete.grid(column='1', padx='5', row='1')
        button_logout = ttk.Button(frame_main)
        button_logout.config(text='Logout')
        button_logout.grid(column='1', padx='5', row='2')

        # Main widget
        self.mainwindow = frame_main

    def run(self):
        self.mainwindow.mainloop()

    def get_credentials(self):
        '''Retrieves all credentials from the database and inserts it into the tree widget'''
        for row in db.show_credentials():
            self.tree.insert("", 'end', text=row['name'], values=(
                row['username'], decrypt_password(row['password'])))

    def select(self, e):
        self.selected_credential = self.tree.item(
            self.tree.selection())['text']

    def delete_credential(self):
        '''Delete credential from database'''
        db.delete_credential(self.selected_credential)
        self.get_credentials()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Password Manager")
    app = MainframeApp(root)
    app.run()
