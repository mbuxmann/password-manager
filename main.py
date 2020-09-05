import tkinter as tk
import tkinter.ttk as ttk
from encryption import encrypted_password, decrypt_password
import backend as db


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(loginRegisterFrame)

    def switch_frame(self, frame_class):
        '''Destroys current frame and replaces it with a new one.'''
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.grid()


class loginRegisterFrame(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.error_message = None

        # Create Label Widgets
        label_username = ttk.Label(self)
        label_username.config(anchor='e', text='Username: ', width='10')
        label_username.grid(padx='5', pady='5', row='1')
        label_password = ttk.Label(self)
        label_password.config(anchor='e', text='Password: ', width='10')
        label_password.grid(padx='5', pady='5', row='2')

        # Create Entry Widgets
        self.entry_username = ttk.Entry(self)
        self.entry_username.grid(column='1', padx='5', pady='5', row='1')
        self.entry_password = ttk.Entry(self, show='*')
        self.entry_password.grid(column='1', padx='5', pady='5', row='2')

        # Create Button Widgets
        button_exit = ttk.Button(self, command=self.exit)
        button_exit.config(text='Exit', width='20')
        button_exit.grid(column='0', padx='5', pady='5', row='3')
        button_login = ttk.Button(self, command=self.login_user)
        button_login.config(text='Login', width='20')
        button_login.grid(column='1', padx='5', pady='5', row='3')

    # loginRegisterFrame Methods
    def exit(self):
        app.destroy()

    def login_user(self):
        '''Takes in a username and password for validation, if successful switch to main frame'''
        if self.entry_username.get().lower() == 'admin' and self.entry_password.get() == 'admin':
            self.master.switch_frame(mainFrame)
        else:
            self.error_message = f'Username / Password Incorrent.'
            self.create_error_label()

    def create_error_label(self):
        '''Creates a label widget to display the error message'''
        label_message = ttk.Label(
            self, foreground='red')
        label_message.config(text=self.error_message)
        label_message.grid(column='0', padx='5',
                           pady='5', row='0', columnspan='2')


class mainFrame(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.selected_credential = None

        # Create Tree widget
        self.tree = ttk.Treeview(self)

        self.tree['columns'] = ('one', 'two')

        self.tree.column('#0')
        self.tree.column('one')
        self.tree.column('two')

        self.tree.heading('#0', text='Name')
        self.tree.heading('one', text='Username')
        self.tree.heading('two', text='Password')

        self.tree.bind('<<TreeviewSelect>>', self.select)

        self.tree.grid(padx='5', pady='5', rowspan='20')

        self.get_credentials()

        # Create Button Widgets
        button_add = ttk.Button(self)
        button_add.config(
            text='Add', command=lambda: master.switch_frame(addCredentialFrame))
        button_add.grid(column='1', padx='5', row='0')
        button_delete = ttk.Button(
            self, command=self.delete_credential)
        button_delete.config(text='Delete')
        button_delete.grid(column='1', padx='5', row='1')
        button_logout = ttk.Button(self)
        button_logout.config(
            text='Logout', command=lambda: master.switch_frame(loginRegisterFrame))
        button_logout.grid(column='1', padx='5', row='2')

    # mainFrame Methods
    def get_credentials(self):
        '''Retrieves all credentials from the database and inserts it into the tree widget'''
        for row in db.show_credentials():
            self.tree.insert('', 'end', text=row['name'], values=(
                row['username'], decrypt_password(row['password'])))

    def select(self, e):
        '''Assigns all selected credentials to selected_credential'''
        self.selected_credential = [self.tree.item(
            x)['text'] for x in self.tree.selection()]

    def delete_credential(self):
        '''Delete all credentials in the selected_credential variable from database'''
        if self.selected_credential == None:
            return

        for item in self.selected_credential:
            db.delete_credential(item)

        self.clear_tree()
        self.get_credentials()

    def clear_tree(self):
        '''Removes all items from the tree widget'''
        for item in self.tree.get_children():
            self.tree.delete(item)


class addCredentialFrame(tk.Frame):
    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.error_message = None

        # Entry Widgets
        self.entry_name = ttk.Entry(self)
        self.entry_name.grid(column='1', padx='5', pady='5', row='1')
        self.entry_username = ttk.Entry(self)
        self.entry_username.grid(column='1', padx='5', pady='5', row='2')
        self.entry_password = ttk.Entry(self)
        self.entry_password.grid(column='1', padx='5', pady='5', row='3')

        # Label Widgets
        label_name = ttk.Label(self)
        label_name.config(anchor='e', text='Name:', width='10')
        label_name.grid(column='0', padx='5', pady='5', row='1')
        label_username = ttk.Label(self)
        label_username.config(anchor='e', text='Username:', width='10')
        label_username.grid(column='0', padx='5', pady='5', row='2')
        label_password = ttk.Label(self)
        label_password.config(anchor='e', text='Password:', width='10')
        label_password.grid(column='0', padx='5', pady='5', row='3')

        # Button Widgets
        button_back = ttk.Button(self)
        button_back.config(text='Back', width='20',
                           command=lambda: master.switch_frame(mainFrame))
        button_back.grid(column='0', padx='5', pady='5', row='4')
        button_add = ttk.Button(self)
        button_add.config(text='Add', width='20', command=self.add_credential)
        button_add.grid(column='1', columnspan='2',
                        padx='5', pady='5', row='4')

    # addCredentialFrame Methods
    def add_credential(self):
        '''Add credential to the database'''
        name = self.entry_name.get()
        username = self.entry_username.get()
        password = self.entry_password.get()

        if not db.check_existance(name) and name != '' and username != '' and password != '':
            password = encrypted_password(password)
            db.add_credential(name, username, password)
            self.master.switch_frame(mainFrame)
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
        '''Creates a label widget to display the error message.'''
        label_message = ttk.Label(
            self, foreground='red')
        label_message.config(text=self.error_message)
        label_message.grid(column='0', padx='5',
                           pady='5', row='0', columnspan='2')


if __name__ == '__main__':
    app = Application()
    app.title('Password Manager')
    app.resizable(False, False)
    app.mainloop()
