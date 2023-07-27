from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

my_email = 'enter your email'
password = 'enter your password'
recipient = ('enter recipient email')
connect_server = SMTP('smtp.gmail.com') #enter hostname for the email service you are using

connect_server.starttls()
connect_server.login(my_email, password)
connect_server.sendmail(from_addr= my_email, to_addrs= recipient, msg='Subject: Hello\n\nThis is a test email from python using automation')
connect_server.close()