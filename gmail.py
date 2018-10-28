import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from httplib2 import Http
 
 
fromaddr = "xyz@gmail.com"
toaddr = "pqr56@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Status Update 28-10-2018"
 
body = "This email is sent via python code"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr,"your password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
