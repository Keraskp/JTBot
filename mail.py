from email.message import EmailMessage
import ssl
import smtplib

app_password = 'lyuocnzjrydizhkn'

email_sender = 'aditya.jobsterritory@gmail.com'
email_password = app_password

email_receiver = 'adityakiran.cs@gmail.com'

subject = 'Python E-mail Sender'
body = """
Hello Sir,

Today, I am trying out Python's email sender. This is the second mail

Thank you

With Regards,
Aditya Kiran Pal
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

