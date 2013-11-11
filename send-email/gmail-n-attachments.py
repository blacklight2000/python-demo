# http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

gmail_user = "xxxman@gmail.com"
gmail_pwd = "PASSWORD"
gmail_mail_server = "smtp.gmail.com"
gmail_mail_server_port = 587

def mail(to, subject, text,attachments):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))
   
   for _attachment in attachments:
      if len(_attachment) > 0:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(_attachment, 'rb').read())
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition',
             'attachment; filename="%s"' % os.path.basename(_attachment))
        msg.attach(part)

   mailServer = smtplib.SMTP(gmail_mail_server, gmail_mail_server_port)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

attachments = ["sniper_cat.jpg","","machine-gun-cat-animation.gif"]
mail("xxxman@yahoo.com",
   "Say Hello now from python!",
   "This is a email sent with python",
   attachments)

