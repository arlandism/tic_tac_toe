from threading import Thread

class ResponseThread(Thread):
  
    def __init__(self, responder):
        super(ResponseThread, self).__init__()
        self.responder = responder

    def run(self):
        self.responder.respond()
