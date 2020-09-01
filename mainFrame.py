import tkinter as tk
import tkinter.ttk as ttk


class MainframeApp:
    def __init__(self, master=None):
        # build ui
        frame_main = ttk.Frame(master)
        frame_main.config(height='600', width='600')
        frame_main.grid()

        treeview_credentials = ttk.Treeview(frame_main)

        # Defining number of columns
        treeview_credentials["columns"] = ("0", "1", "2")

        # Assigning the width and anchor to  the
        # respective columns
        treeview_credentials.column("0", width=90, anchor='c')
        treeview_credentials.column("1", width=90, anchor='c')
        treeview_credentials.column("2", width=90, anchor='c')

        # Assigning the heading names to the
        # respective columns
        treeview_credentials.heading("0", text="Name")
        treeview_credentials.heading("1", text="Sex")
        treeview_credentials.heading("2", text="Age")

        treeview_credentials.grid(padx='5', pady='5', rowspan='20')

        treeview_credentials.insert("", 'end', text="L1",
                                    values=("Nidhi", "F", "25"))
        treeview_credentials.insert("", 'end', text="L2",
                                    values=("Nisha", "F", "23"))
        treeview_credentials.insert("", 'end', text="L3",
                                    values=("Preeti", "F", "27"))

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

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("Password Manager")
    app = MainframeApp(root)
    app.run()
