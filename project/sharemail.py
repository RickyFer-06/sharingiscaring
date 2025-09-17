import smtplib
import time
from module import *

url_code = open("project/url_df.txt")
url = f"https://docs.google.com/spreadsheets/d/{url_code.read()}/export?format=csv"

subject = define_subject()
list = define_list(url)
server = smtplib.SMTP("smtp.gmail.com", 587)
email = "partners.shareup@gmail.com" #Alterar consoante email aqui.
server.starttls()
server.login(email, "ttvy qbux efwh exil ") #Alterar consoante email aqui.
    
for i in range(0,len(list),2):
    name_receiver = list[i]
    email_receiver = list[i+1]
    email_sender(email_receiver, name_receiver, subject, email, server)
    time.sleep(0.5)
