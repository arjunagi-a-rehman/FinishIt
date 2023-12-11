from flask_mail import Mail,Message
from todoapp import app1 as app

mail = Mail(app) 
def send_mail(subject, sender, recipients, body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = body
    with app.app_context():
        mail.send(msg)