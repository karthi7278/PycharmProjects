from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

msg=MIMEMultipart()

password="devikamakshi"
message="O'Rielly :P"
msg["From"]="karthi7278@gmail.com"
msg["To"]="naveenbabumallepudi@gmail.com"
msg["Subject"]="Test Mail"

msg.attach(MIMEText(message,"plain"))

server=smtplib.SMTP("smtp.gmail.com","587")
server.starttls()
server.login(msg["From"],password)
server.sendmail(msg["From"],msg["To"],msg.as_string())
server.quit()
print("Message has been sent successfully to",msg["To"])





