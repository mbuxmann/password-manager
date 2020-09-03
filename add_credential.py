import tkinter as tk
import tkinter.ttk as ttk
import backend as db
from encryption import encrypted_password


class AddcredentialsApp:
    def __init__(self, master=None):
        self.error_message = None

        # build ui
        self.frame_add = ttk.Frame(master)
        self.frame_add.config(height='600', width='600')
        self.frame_add.grid()

        # Entry Widgets
        self.entry_name = ttk.Entry(self.frame_add)
        self.entry_name.grid(column='1', padx='5', pady='5', row='1')
        self.entry_username = ttk.Entry(self.frame_add)
        self.entry_username.grid(column='1', padx='5', pady='5', row='2')
        self.entry_password = ttk.Entry(self.frame_add)
        self.entry_password.grid(column='1', padx='5', pady='5', row='3')

        # Label Widgets
        label_name = ttk.Label(self.frame_add)
        label_name.config(anchor='e', text='Name:', width='10')
        label_name.grid(column='0', padx='5', pady='5', row='1')
        label_username = ttk.Label(self.frame_add)
        label_username.config(anchor='e', text='Username:', width='10')
        label_username.grid(column='0', padx='5', pady='5', row='2')
        label_password = ttk.Label(self.frame_add)
        label_password.config(anchor='e', text='Password:', width='10')
        label_password.grid(column='0', padx='5', pady='5', row='3')

        # Button Widgets
        button_back = ttk.Button(self.frame_add)
        button_back.config(text='Back', width='20')
        button_back.grid(column='0', padx='5', pady='5', row='4')
        button_add = ttk.Button(self.frame_add)
        button_add.config(text='Add', width='20', command=self.add_credential)
        button_add.grid(column='1', columnspan='2',
                        padx='5', pady='5', row='4')

        # Main widget
        self.mainwindow = self.frame_add

    def run(self):
        self.mainwindow.mainloop()

    def add_credential(self):
        '''Add credential to database'''
        name = self.entry_name.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not db.check_existance(name) and name != '' and username != '' and password != '':
            password = encrypted_password(password)
            db.add_credential(name, username, password)
            return

        if name == '':
            self.error_message = 'Please enter in a valid name!'
        elif db.check_existance(name):
            self.error_message = f'{name.title()} already exists!'
        elif username == '':
            self.error_message = f'Please enter in a valid username'
        elif password == '':
            self.error_message = f'Please enter in a valid password!'

        self.create_error_label()

    def create_error_label(self):
        label_message = ttk.Label(
            self.frame_add, foreground='red')
        label_message.config(text=self.error_message)
        label_message.grid(column='0', padx='5',
                           pady='5', row='0', columnspan='2')


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Add Credential')
    app = AddcredentialsApp(root)
    app.run()
