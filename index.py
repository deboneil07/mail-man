import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(email, password, receiver):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    server = smtplib.SMTP(host=smtp_server, port=smtp_port)
    server.starttls()

    server.login(email, password)

    message = MIMEMultipart()
    message["From"] = email
    message["To"] = receiver
    message["Subject"] = "Test Email for App"
    body = "Hi, this is a test email, thanks for reading. Have a great day."
    message.attach(MIMEText(body, 'plain'))

    server.sendmail(email, receiver, message.as_string())
    server.quit()
    
if __name__ == "__main__":
    email = os.getenv("MY_EMAIL")
    password = os.getenv("MY_PASS")
    receiver = "db1833@srmist.edu.in"

    try:
        send_mail(email, password, receiver)
        print("sent successfully!")
        
    except Exception as e:
        print("error sending mail", e)