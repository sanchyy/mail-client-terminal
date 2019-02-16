class User:
    def __init__(self):
        self.mail = ""
        self.password = ""
    
    def __init__(self,mail,password):
        self.mail = mail
        self.password = password

    def set_user(self,mail):
        self.mail = mail

    def set_password(self,password):
        self.password = password

    
