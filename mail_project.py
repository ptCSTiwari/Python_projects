# Python_projects
'''after a hard work on learning python i have tried to make some projects.'''

import smtplib

try:
    server = smtplib.SMTP("smtp.gmail.com", port=587)
    server.starttls()  # Start TLS encryption

    receiver_mail = input("Enter receiver's email address: ")

    # Email credentials
    sender_mail = "put your email here" 
    password = "generate one time password and put here"  # App password

    # Login
    server.login(sender_mail, password)

    # Compose email
    subject = input("Enter subject: ")
    body = input("Enter message body: ")
    message = f"Subject: {subject} \n\n {body}"

    # Send email
    server.sendmail(sender_mail, receiver_mail, message)
    print("Mail sent successfully!")

    server.quit()
except Exception as e:
    print("An error occurred:", e)
