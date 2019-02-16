from '.' import user

class Mail:
    def __init__(self):
        self.service = ""
        self.user = User()
        self.sender = ""
        self.message = ""

    def __init__(self,service,user,sender,message):
        self.service = service
        self.user = user
        self.sender = sender
        self.message = message

    def set_service(self,service):
        self.service = service

    def set_user(self,mail):
        self.user = user

    def set_sender(self,sender):
        self.sender = sender

    def set_message(self,message):
        self.message = message
