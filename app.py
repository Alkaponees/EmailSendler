import smtplib
from email.mime.text import MIMEText
def send_email(subject, body, sender, recipients, password, number):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    
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