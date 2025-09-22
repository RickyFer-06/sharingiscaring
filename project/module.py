import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def capitalize_string(name):
    name = name.casefold()
    name = name.capitalize()
    result = name[0]
    list = []
    for j in name:
        list.append(j)
    for i in range(1,len(list)):
        if list[i-1] == " ":
            list[i] = list[i].upper()
        result += list[i]
    return result

def define_subject():
    assunto = open("project/subject_df.txt", encoding="UTF-8")
    assunto = assunto.read()
    return assunto

def define_list(url):
    list = []
    df = pd.read_csv(url, encoding="UTF-8")
    emails = df["Email"].dropna().tolist()
    nomes = df["Nome"].dropna().tolist()
    
    for i in range(len(emails)):
        list.append(capitalize_string(nomes[i],))
        list.append(emails[i])

    return list

#Aqui é possível realizar-se a alteração da mensagem do email.
def define_message (name):
    message = f"""
        Bom dia, {name}!
        
        Confirmamos a tua inscrição no evento!
        
        Cumprimentos,
        ShARE-UP."""
    return message

def email_sender (email_receiver, name_receiver, subject, email, server):
    msg = define_message(name_receiver)
    msg = MIMEText(msg, "plain", "UTF-8")
    msg["Subject"] = subject
    msg["X-Priority"] = "1" #Alterar a importância do email
    msg["Importance"] = "High" #Alterar a importância do email
    msg["Reply-To"] = email
    msg['From'] = email
    msg['To'] = email_receiver


    server.sendmail(email, email_receiver, msg.as_string())
    print("Email sent to: " + name_receiver + "\n" + email_receiver)
    print("\n")
    return