import tkinter as tk
import tkinter.ttk as ttk


class loginRegister:

    def __init__(self, master=None):

        # Build UI
        frame_start = ttk.Frame(master)
        frame_start.config(height='600', width='600')
        frame_start.grid()

        label_username = ttk.Label(frame_start)
        label_username.config(anchor='e', text='Username: ', width='10')
        label_username.grid(padx='5', pady='5')
        label_password = ttk.Label(frame_start)
        label_password.config(anchor='e', text='Password: ', width='10')
        label_password.grid(padx='5', pady='5', row='1')

        self.entry_username = ttk.Entry(frame_start)
        self.entry_username.grid(column='1', padx='5', pady='5', row='0')
        self.entry_password = ttk.Entry(frame_start, show="*")
        self.entry_password.grid(column='1', padx='5', pady='5', row='1')

        button_register = ttk.Button(frame_start, command=self.register_user)
        button_register.config(text='Register', width='20')
        button_register.grid(column='0', padx='5', pady='5', row='2')
        button_register.rowconfigure('2', minsize='0')
        button_login = ttk.Button(frame_start, command=self.login_user)
        button_login.config(text='Login', width='20')
        button_login.grid(column='1', padx='5', pady='5', row='2')
        button_login.rowconfigure('2', minsize='0')

        # Main widget
        self.mainwindow = frame_start

    def run(self):
        self.mainwindow.mainloop()

    # Functions
    def register_user(self):
        print(self.entry_username.get(), self.entry_password.get())

    def login_user(self):
        '''Takes in a username and password for validation and then logs user in'''
        if self.entry_username.get().lower() == "bitvivaz" and self.entry_password.get() == "123":
            print("True")
            return True
        else:
            print("False")
            return False


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Password Manager")
    app = loginRegister(root)
    app.run()
