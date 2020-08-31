import tkinter as tk
import tkinter.ttk as ttk


class Application:

    def __init__(self, master=None):
        self.username = tk.StringVar

        # build ui
        frame_start = ttk.Frame(master)
        label_username = ttk.Label(frame_start)
        label_username.config(anchor='e', text='Username: ', width='10')
        label_username.grid(padx='5', pady='5')
        label_password = ttk.Label(frame_start)
        label_password.config(anchor='e', text='Password: ', width='10')
        label_password.grid(padx='5', pady='5', row='1')
        entry_username = ttk.Entry(frame_start, textvariable=self.username)
        entry_username.config(justify='left')
        entry_username.grid(column='1', padx='5', pady='5', row='0')
        entry_password = ttk.Entry(frame_start)
        entry_password.grid(column='1', padx='5', pady='5', row='1')
        button_register = ttk.Button(
            frame_start, command=lambda: validate_user(entry_username.get(), entry_password.get()))
        button_register.config(text='Register', width='20')
        button_register.grid(column='0', padx='5', pady='5', row='2')
        button_register.rowconfigure('2', minsize='0')
        button_login = ttk.Button(frame_start)
        button_login.config(text='Login', width='20')
        button_login.grid(column='1', padx='5', pady='5', row='2')
        button_login.rowconfigure('2', minsize='0')
        frame_start.config(height='600', width='600')
        frame_start.grid()

        # Main widget
        self.mainwindow = frame_start

        def validate_user(username, password):
            print(username, password)

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Password Manager")
    app = Application(root)
    app.run()
