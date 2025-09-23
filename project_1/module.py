import smtplib
import pandas as pd
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def capitalize_string(name):
    return ' '.join(word.capitalize() for word in name.lower().split())

def define_subject():
    with open("project_1/subject_df.txt", encoding="UTF-8") as file:
        return file.read().strip()

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
<html>

    <body>
        <p>Olá, {name}!</p>
        <br>
        <p>Gostaríamos de confirmar a tua inscrição no Perspetivas, edição 2025.</p>
        <br>
        <p>Cumprimentos,
            Equipa de CR.
        </p>
        <img src="cid:myimage" style="width: 400px;">
    </body>
</html>"""
    return message

def email_sender (email_receiver, name_receiver, subject, email, server):
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["X-Priority"] = "3" #Alterar a importância do email
    #msg["Importance"] = "High"
    msg["Reply-To"] = email
    msg['From'] = email
    msg['To'] = email_receiver
    txt = define_message(name_receiver)
    txt = MIMEText(txt, "html", "UTF-8",)
    msg.attach(txt)

    image = open("project_1/share.png","rb")
    image = image.read()
    image = MIMEImage(image,name="SHARE")
    image.add_header("Content-ID","<myimage>")
    image.add_header("Content-Disposition","inline",filename="project_1/share.png")
    msg.attach(image)


    server.sendmail(email, email_receiver, msg.as_string())
    print("Email sent to: " + name_receiver + "\n" + email_receiver)
    print("\n")
    return