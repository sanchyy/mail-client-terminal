import json
import os
from email.mime.text import MIMEText
import smtplib
import imaplib
import getpass

PORT = 587

def services():
    with open('services.json','w') as f:
        data = json.load(f)
        for k,v in data:
            print('[{}] {}'.format(k,v))
        print('[{}] new one'.format(data.length+1))
        opt = input('> ')
        if opt == data.length+1:
            new_op = input('new smtp service: ')
            data.update({data.length+1,new_op})
            f.write(data)
            return new_op

        return data[opt]
            

def set_user():
    _user = User()
    user.mail = input('mail: ')
    user.password = getpass.getpass('password: ')
    return user

def set_mail():
    mail = Mail()
    mail.service = services()
    mail.user = user
    mail.sender = str(input("A qui vols enviar l'e-mail"))
    with open('msg_to_{}.txt'.format(mail['To'].split('@')[0]),'w') as f:
        f.write('SUBJECT: ')
    os.system('vi msg_to_{}.txt'.format(mail['To'].split('@')[0])) 
    with open('msg_to_{}.txt'.format(mail.sender.split('@')[0]),'w') as f:
        mail.subj = f.readline()
        message = f.read().splitlines(True)
        mail.msg = message[1:]
    return mail
    

def send_mail(m):
    mailserver = smtplib.SMTP(m.service,PORT)
    mailserver.ehlo()
    mailserver.starttls()  
    mailserver.ehlo()
    mailserver.login(m.user.mail,m.user.password)
    #mailserver.sendmail('')
    mailserver.quit()

def view_inbox():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(user.mail,user.password)
    inboxes = mail.list()
    return  

if __name__ == '__main__':
    m = Mail()
    user = User()
    mail
    
    while 1:
        option = str(input("> ")).lower()
        if option == 'help':
            print('what to do...')    

        elif option == 'set-user':
            user = set_user()
            
        elif option == 'send-mail':
            if user.mail == "":
                print("define user before sending mail")
            else:
                m = set_mail()
                send_mail(m)

        elif: option == 'inbox':
            if user.mail == "":
                print("Primer fes login!")
            else:
               view_inbox(m)

        else:
            print('Not a possible action, type help for information')
