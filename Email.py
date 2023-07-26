from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

my_email = 'k213815@nu.edu.pk'
password = 'hamzaowais.1'
recipient = ('k213815@nu.edu.pk','k213828@nu.edu.pk','k213838@nu.edu.pk')
connect_server = SMTP('smtp.gmail.com')

connect_server.starttls()
connect_server.login(my_email, password)
connect_server.sendmail(from_addr= my_email, to_addrs= recipient, msg='Subject: Hello\n\nThis is a test email from python using automation')
connect_server.close()