import smtplib
import os
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "gmailaddress@"
    password = "special gmail password"
    receiver = "gmailaddress@"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)