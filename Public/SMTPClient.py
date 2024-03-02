import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SMTPClient:
    def __init__(self, smtp_server, port, username, password):
        self.smtp_server = smtp_server
        self.port = port
        self.username = username
        self.password = password
        self.server = None

    def connect(self):
        self.server = smtplib.SMTP(self.smtp_server, self.port)
        self.server.starttls()
        self.server.login(self.username, self.password)

    def send_email(self, sender, recipients, subject, body):
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = ", ".join(recipients)
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))
        self.server.sendmail(sender, recipients, message.as_string())

    def disconnect(self):
        if self.server:
            self.server.quit()
