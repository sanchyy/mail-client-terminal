from '.' import mail
import json

#service = json a carregar

def services():
    with open(services.json,'w') as f:
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
            
    

if __name__ == '__main__':
    while 1:
        option = input("> ")
        if option.lower() == 'help':
            print('what to do...')    
        elif option.lower() == 'set-user':
            us = input('mail: ')
            pw = input('password: ')
        
        elif option.lower() == 'send-mail'
            if user.mail == "":
                print("define user before sending mail")
            else:
                email.service = services()
                email.user
               
                

