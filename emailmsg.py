import smtplib

sender = "asimriazasim107@gmail.com"
receiver = "sohailriazveh107@gmail.com"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is test to cheack notification through email in python code."""

with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
    server.login("ce267c3937b1b7", "ad85f44f11bcfb")
    server.sendmail(sender, receiver, message)