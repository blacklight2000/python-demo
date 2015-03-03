# http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html

import smtplib
from email import MIMEMultipart
from email import MIMEBase
from email import MIMEText
from email import Encoders
import os

yahoo_mail_user = "xxxman@yahoo.com"
yahoo_mail_pwd = "PASSWORD"

def mail(to, subject, text, attach):
    msg = MIMEMultipart()

    msg['From'] = yahoo_mail_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload(open(attach, 'rb').read())
    # Encoders.encode_base64(part)
    # part.add_header('Content-Disposition',
    #        'attachment; filename="%s"' % os.path.basename(attach))
    # msg.attach(part)

    mailServer = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    # mailServer.ehlo()
    # mailServer.starttls()
    # mailServer.ehlo()
    mailServer.login(yahoo_mail_user, yahoo_mail_pwd)
    mailServer.sendmail(yahoo_mail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()

mail("xxxman@yahoo.com",
    "Say Hello now from python!",
    "This is a email sent with python",
    "")
