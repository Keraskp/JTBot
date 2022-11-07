from email.message import EmailMessage
import ssl
import smtplib


class Mailer:

    __app_password = 'lyuocnzjrydizhkn'

    def __init__(self, receiver, details):
        self.sender = 'aditya.jobsterritory@gmail.com'
        self.receiver = receiver
        self.details = details
        self.subject = 'JTBot Support Call'
        self.body = """
Dear Team,

A brand-new user signed up for Jobs Territory. Requesting communication from the support team.
Customer Details:
Name : {name}
Email : {email}
Phone : {phone}
Service : {service}

Thank you

With Regards,
JTBot
""".format(name=self.details.get('name'), email=self.details.get('email'), phone=self.details.get('phone'), service=self.details.get('service_type'))
    
    def mail(self):
        em = EmailMessage()
        em['From'] = self.sender
        em['To'] = self.receiver
        em['subject'] = self.subject
        em.set_content(self.body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
            smtp.login(self.sender, Mailer.__app_password)
            smtp.sendmail(self.sender, self.receiver, em.as_string())
