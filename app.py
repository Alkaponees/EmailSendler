import smtplib
from email.mime.text import MIMEText
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

with open("attachment.txt", "rb") as attachment:
    # Add the attachment to the message
    part = MIMEBase("application", "octet-stream")
    part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {os.path.basename('attachment.txt')}",
)

def send_email(subject, body, sender, recipients, password, number):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    
    msg.attach(part)
    for i in range(number):
        smtp_server = smtplib.SMTP_SSL('smtp.ukr.net', 465)
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
        print(i)
        smtp_server.quit()
subject = "Email Subject"
body = """Hi Friend,
I'm just testing my program right now. Please feel free to ignore this email.
Thanks,
Your Name Here
"""
sender = "mr.sergey1898@ukr.net"
r_reader= open('recepients.txt','r')
recipients = []
for i in r_reader:
    recipients.append(i)
p_reader = open('password.txt','r')
password= None
for i in p_reader:
    password = i
number = int(input("Enter number of letters... "))
send_email(subject, body, sender, recipients, password, number)