import json
import smtplib
from email.message import EmailMessage

# Loading the secret data from secret.json file
with open('secret.json') as f:
    secret_data = json.load(f)

smtp_server = secret_data['smtp_server']
smtp_port = secret_data['smtp_port']
smtp_username = secret_data['smtp_username']
smtp_password = secret_data['smtp_password']
receiver = secret_data['receiver']

# Read the contents of your HTML template
with open('template.html') as f:
    html = f.read()

# Create the message
msg = EmailMessage()
msg['Subject'] = 'Hi smtplib'
msg['From'] = smtp_username
msg['To'] = receiver
msg.set_content('This is a test email for python Library.don it')
msg.add_alternative(html, subtype='html')

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
