import json
import smtplib
from email.message import EmailMessage

# Loading the secret data from  secret.json file
with open('secret.json') as f:
    secret_data = json.load(f)


smtp_server = secret_data['smtp_server']
smtp_port = secret_data['smtp_port']
smtp_username = secret_data['smtp_username']
smtp_password = secret_data['smtp_password']
receiver = secret_data['receiver']

# Create the  message
msg = EmailMessage()
msg['Subject'] = 'Hi smtplib'
msg['From'] = smtp_username
msg['To'] = receiver
msg.set_content('This is a test email for python Library.')


with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
