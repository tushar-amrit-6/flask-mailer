from flask import Flask
from flask_mail import Mail, Message
import pandas as pd

## not imortant

app =Flask(__name__)
mail=Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'tusharpubg02@gmail.com'
app.config['MAIL_PASSWORD'] = '*********'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route("/")
def index():
   msg = Message('Hello', sender = 'tusharpubg02@gmail.com', recipients = ['tushar.amrit.6@gmail.com'])
   msg.body = "A mail to implement flask_mail"
   mail.send(msg)
   return "Message Sent "

if __name__ == '__main__':
   app.run(debug = True)
