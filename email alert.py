import smtplib
from email.message import EmailMessage

def email_alert(subject,body,to):
    msg = EmailMessage()
    msg.set_content(body)

    msg["subject"] = subject
    msg["to"] = to

    admin = "flaskauthenticationproject@gmail.com"
    msg["from"] = admin
    password = "pkzxrcbsnmpotnjd"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(admin, password)
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    email_alert("Unauthorized Login Attempt", "There was an attempt to access this file by an unauthorized person",
                "flaskauthenticationproject@gmail.com")
