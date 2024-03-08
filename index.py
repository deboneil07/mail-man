from tkinter import *
from tkinter import ttk
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os



login_header = ('Arial', 12, 'bold')
class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.title("Mailman")
        self.login()

    def login(self):
        for i in self.root.winfo_children():
            i.destroy()
        self.frame1 = Frame(self.root, width=400, height=400)
        for i in range(4):
            self.frame1.rowconfigure(i, minsize=80, weight=1)
        for i in range(3):
            self.frame1.columnconfigure(i, minsize=100, weight=1)
        self.frame1.pack()
        self.lbl_intro_text = ttk.Label(self.frame1, text="Welcome to Mailman", font=("sans-serif", 14))
        self.lbl_intro_text.grid(row=0, column=1)

        self.entry_gmail = ttk.Entry(self.frame1)
        self.entry_gmail.grid(row=1, column=1, sticky="ew", columnspan=2)

        self.lbl_gmail = ttk.Label(self.frame1, text="Email Address", foreground="green", font=('Helvetica', 10))
        self.lbl_gmail.grid(row=1, column=0)

        self.entry_password = ttk.Entry(self.frame1, show="*")
        self.entry_password.grid(row=2, column=1, sticky="ew", columnspan=2)

        self.lbl_password = ttk.Label(self.frame1, text="App Password", foreground="green", font=('Helvetica', 10))
        self.lbl_password.grid( row=2, column=0)

        


        





root = Tk()
App(root)
root.mainloop()