from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk
import webbrowser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv, set_key

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mailman")  
        self.confirm()
        # self.error()
        #self.login()

    def login(self):
        for i in self.root.winfo_children():
            i.destroy()
        self.root.geometry("400x400")
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
            if ((mail != "") and (password != "")):
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
        user_gmail = self.entry_gmail.get()
        user_password = self.entry_password.get()
        
        set_key(".env", 'MY_EMAIL', user_gmail)
        set_key(".env", 'MY_PASSWORD', user_password)

        load_dotenv(override=True) # allowing env to override the values

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

        self.btn_back = ttk.Button(self.frame2, text="Back", command=self.login)
        self.btn_back.grid(row=4, column=0)

        self.btn_send = ttk.Button(self.frame2, text="Send", command=self.server_run)
        self.btn_send.grid(row=4, column=1, sticky="ew")
        
        self.btn_reset = ttk.Button(self.frame2, text="Reset", command=self.main_reset)
        self.btn_reset.grid(row=4, column=2)

    def server_run(self):
        self.mail_send(os.getenv('MY_EMAIL'), os.getenv('MY_PASSWORD'), self.entry_sub, self.entry_to, self.entry_body)
        if (self.mail_send == True):
            self.confirm()
        else:
            self.error()

    def error(self):
        for i in self.root.winfo_children():
            i.destroy()
        self.root.geometry("400x400")
        self.frame_err = ttk.Frame(self.root, width=400, height=400)
        self.frame_err.pack()
        for i in range(4):
            self.frame_err.rowconfigure(i, minsize=80, weight=1)
        self.frame_err.columnconfigure(0, minsize=100, weight=1)

        self.lbl_header = ttk.Label(self.frame_err, text=":\ ERROR 404 ;-;", font=("Helvetica", 28))
        self.lbl_header.grid(row=1, column=0)

        self.lbl_para = ttk.Label(self.frame_err ,font=("Sans", 12) ,text="\nThere was an issue with sending the mail. \n\nPlease check your credentials and try again.")
        self.lbl_para.grid(row=2, column=0)

        self.lbl_back = ttk.Label(self.frame_err, foreground="blue",text="go back to login page", cursor="hand2" ,font=("Sans", 12))
        self.lbl_back.grid(row=4, column=0)
        self.lbl_back.bind("<Button-1>", lambda event: self.login())

        # self.root.after(1000, self.error)



    def confirm(self):
        for i in self.root.winfo_children():
            i.destroy()
        self.root.geometry("400x400")
        self.frame_con = ttk.Frame(self.root, height=600, width=600)
        self.frame_con.pack()
        for i in range(4):
            self.frame_con.rowconfigure(i, minsize=80, weight=1)
        self.frame_con.columnconfigure(0, minsize=100, weight=1)

        self.lbl_header = ttk.Label(self.frame_con, text="Mail sent successfully!", font=("Helvetica", 28))
        self.lbl_header.grid(row=1, column=0)

        self.lbl_para = ttk.Label(self.frame_con ,font=("Sans", 12) ,text="\nYour mail has been sent successfully.\n ")
        self.lbl_para.grid(row=2, column=0)

        self.lbl_para2 = ttk.Label(self.frame_con, font=("Sans", 12), text="Thanks for using Mailman !")
        self.lbl_para2.grid(row=3, column=0)

        self.lbl_back = ttk.Label(self.frame_con, foreground="blue",text="go back to login page", cursor="hand2" ,font=("Sans", 12))
        self.lbl_back.grid(row=4, column=0)
        self.lbl_back.bind("<Button-1>", lambda event: self.login())


    def mail_send(self, my_gmail, my_password, subject, to, body):
        try:
            gmail_server = "smtp.gmail.com"
            gmail_port = 587

            mailing_server = smtplib.SMTP(gmail_server, gmail_port)
            mailing_server.ehlo()
            mailing_server.starttls()
            mailing_server.login(user=my_gmail, password=my_password)

            message = MIMEMultipart()
            message['Subject'] = subject
            message.attach(MIMEText(body))

            mailing_server.sendmail(
                from_addr=my_gmail,
                to_addrs=to,
                msg=message.as_string()
            )

            mailing_server.quit()
            return True
        except Exception:
            return False


    def main_reset(self):
        self.entry_to.delete(0, tk.END)
        self.entry_sub.delete(0, tk.END)
        self.entry_body.delete("1.0", tk.END)

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


if __name__ == "__main__":
    root = Tk()
    App(root)
    root.mainloop()