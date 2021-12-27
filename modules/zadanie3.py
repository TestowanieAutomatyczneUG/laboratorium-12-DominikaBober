
class Messenger:

    def __init__(self, sender):
        self.template_engine = TemplateEngine()
        self.mail_server = MailServer()
        self.sender = sender
    
    def send_message(self, receiver, message):
        template = self.template_engine.create_template(receiver, message)
        return self.template_engine.send(template, self.mail_server)
    
    def receive_message(self):
        return self.template_engine.receive(self.sender, self.mail_server)

'''
W mojej głowie wygląda to tak, ze:
    TemplateEngine ma create_template co bierze nadawce i wiadomość i robi sobie templatkę,
    send bierze te templatke i MailServer i jakoś to wysyła i tam sb zwróci status 200,
    a receive bierze sobie osobę i łącząc sie z MailServer pobiera dla niej wiadomości.
Idk
'''

class TemplateEngine:
    def send(self, template, mail_server):
        pass
    def receive(self, user, mail_server):
        pass
    def create_template(self, receiver, message):
        pass

class MailServer:
    pass