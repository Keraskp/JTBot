from email.message import EmailMessage
import ssl
import smtplib
from datetime import date


class Mailer:

    app_password = 'lyuocnzjrydizhkn'

    def __init__(self):
        self.sender = 'aditya.jobsterritory@gmail.com'
        self.receiver = None
        self.date = date.today().strftime("%d/%m/%Y")
        self.subject = f'Progress as of {self.date}'
        self.salutation = 'Sir'
        self.body = """
Hello {salute},

Today, I am trying out Python's email sender. This is the second mail
Thank you

With Regards,
Aditya Kiran Pal
        """.format(salute=self.salutation)

    def mail(self, receiver):
        self.receiver = receiver
        em = EmailMessage()
        em['From'] = self.sender
        em['To'] = self.receiver
        em['subject'] = self.subject
        em.set_content(self.body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(self.sender, Mailer.app_password)
            smtp.sendmail(self.sender, self.receiver, em.as_string())

        self.receiver = None


if __name__ == "__main__":
    email = Mailer()
    email.mail('adityakiran.cs@gmail.com')
    email.mail('suggi.aditya@gmail.com')
    print(email.body)
