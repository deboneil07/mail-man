from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

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
        for i in range(5):
            self.frame1.rowconfigure(i, minsize=80, weight=1)
        for i in range(3):
            self.frame1.columnconfigure(i, minsize=100, weight=1)
        self.frame1.pack()
        self.lbl_intro_text = ttk.Label(self.frame1, text="Welcome to Mailman", font=("sans-serif", 14))
        self.lbl_intro_text.grid(row=0, column=1)

        self.entry_gmail = ttk.Entry(self.frame1)
        self.entry_gmail.grid(row=1, column=1, sticky="ew", columnspan=2)

        self.lbl_gmail = ttk.Label(self.frame1, text="Email Address", font=('Helvetica', 10))
        self.lbl_gmail.grid(row=1, column=0)
        self.entry_gmail.bind("<FocusIn>", self.lbl_gmail_active)
        self.entry_gmail.bind("<FocusOut>", self.lbl_gmail_inactive)

        self.entry_password = ttk.Entry(self.frame1, show="*")
        self.entry_password.grid(row=2, column=1, sticky="ew", columnspan=2)

        self.lbl_password = ttk.Label(self.frame1, text="App Password", font=('Helvetica', 10))
        self.lbl_password.grid( row=2, column=0)
        self.entry_password.bind("<FocusIn>", self.lbl_password_active)
        self.entry_password.bind("<FocusOut>", self.lbl_password_inactive)

        self.lbl_help_link = ttk.Label(self.frame1, text="What is App Password?", foreground="blue", cursor="hand2")
        self.lbl_help_link.bind("<Button-1>", self.help_link)
        self.lbl_help_link.grid(row=3, column=1)   

        self.btn_login = ttk.Button(self.frame1, text="Login", command=self.auth)
        self.btn_login.grid(row=4, column=1, sticky="ew")

        self.btn_reset = ttk.Button(self.frame1, text="Reset", command=self.reset)
        self.btn_reset.grid(row=4, column=2)

    def auth(self):
        try:
            mail = self.entry_gmail.get()
            password = self.entry_password.get()
            if ((mail == "") and (password == "")): ## remember to change this auth part
                print("auth pass")
                self.main()
            else:
                self.login()
                raise ValueError("\nmissing or wrong credentials")
        except ValueError as e:
            print("auth failed", e)

    def reset(self):
        self.entry_gmail.delete("0", tk.END)
        self.entry_password.delete("0", tk.END)

    def main(self):
        for i in self.root.winfo_children():
            i.destroy()
        self.root.geometry("600x600")
        self.frame2 = ttk.Frame(self.root, width=600, height=600)
        for i in range(5):
            self.frame2.rowconfigure(i, minsize=80, weight=1)
        for i in range(3):
            self.frame2.columnconfigure(i, minsize=100, weight=1)
        self.frame2.pack()

        self.lbl_head = ttk.Label(self.frame2, text="Compose Mail", font=("Arial", 20))
        self.lbl_head.grid(row=0, column=1)

        self.lbl_to = ttk.Label(self.frame2, text="To", font=("Arial", 14))
        self.lbl_to.grid(row=1, column=0)

        self.entry_to = ttk.Entry(self.frame2, width=60, font=("Helvetica", 12))
        self.entry_to.grid(row=1, column=1, sticky="ew")

        self.lbl_sub = ttk.Label(self.frame2, text="Subject",font=("Helvetica", 14))
        self.lbl_sub.grid(row=2, column=0)

        self.entry_sub = ttk.Entry(self.frame2, width=60, font=("Sans", 12))
        self.entry_sub.grid(row=2, column=1, sticky=tk.EW)

        self.lbl_body = ttk.Label(self.frame2, text="Body", font=("Sans", 14))
        self.lbl_body.grid(row=3, column=0, sticky="n")

        self.entry_body = tk.Text(self.frame2, height=100, width=60, font=("Sans", 11))
        self.entry_body.grid(row=3, column=1, sticky="ew")



    def help_link(self, event):
        webbrowser.open("https://support.google.com/mail/answer/185833?hl=en#:~:text=Go%20to%20your%20Google%20Account,the%20page%2C%20select%20App%20passwords.", 0)


    def lbl_gmail_active(self, event):
        self.lbl_gmail.config(foreground="green")

    def lbl_gmail_inactive(self, event):
        self.lbl_gmail.config(foreground="black")

    def lbl_password_active(self, event):
        self.lbl_password.config(foreground="green")

    def lbl_password_inactive(self, event):
        self.lbl_password.config(foreground="black")


root = Tk()
App(root)
root.mainloop()