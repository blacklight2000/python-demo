# http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os
import json

email_user_hash = '{ "yahoo":"xxxman@yahoo.com", "gmail":"xxxman@gmail.com"}' 
email_pwd_hash = '{ "yahoo":"PASSWORD","gmail":"PASSWORD" }'
email_mail_server_hash = '{ "yahoo":"smtp.mail.yahoo.com","gmail":"smtp.gmail.com"}'
email_mail_server_port_hash = '{ "yahoo":587, "gmail":587 }'
email_starttls_auth_hash = '{ "yahoo":0,"gmail":1 }'

email_user = json.loads(email_user_hash)
email_pwd = json.loads(email_pwd_hash)
email_mail_server = json.loads(email_mail_server_hash)
email_mail_server_port = json.loads(email_mail_server_port_hash)
email_starttls_auth = json.loads(email_starttls_auth_hash)

def mail(carrier, to, subject, text,encoding,attachments):
   msg = MIMEMultipart()

   msg['From'] = email_user[carrier]
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text,encoding))
   
   
   for _attachment in attachments:
      if len(_attachment) > 0:
         part = MIMEBase('application', 'octet-stream')
         part.set_payload(open(_attachment, 'rb').read())
         Encoders.encode_base64(part)
         part.add_header('Content-Disposition',
             'attachment; filename="%s"' % os.path.basename(_attachment))
         msg.attach(part)

   mailServer = smtplib.SMTP(email_mail_server[carrier], 
                                     email_mail_server_port[carrier])
   if email_starttls_auth[carrier] == 1:
      mailServer.ehlo()
      mailServer.starttls()
      mailServer.ehlo()

   mailServer.login(email_user[carrier], email_pwd[carrier])
   mailServer.sendmail(email_user[carrier], to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

attachments = ["sniper_cat.jpg","","machine-gun-cat-animation.gif"]
# carrier = "gmail"
recipient = "xxxman@yahoo.com"
subject = "Say Hello now from Python!"
message1 = "This is an email sent with Python"
message2 = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
       <h3><b>HFHF</b></h3>
    </p>
  </body>
</html>
"""
mail("yahoo",recipient, subject, message1,'plain', attachments)
mail("gmail",recipient, subject, message1,'plain', attachments)
mail("yahoo",recipient, subject, message2,'html', attachments)
mail("gmail",recipient, subject, message2,'html', attachments)



