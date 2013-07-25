
class SocketInput(object):
    
    def __init__(self,socket):
        self.socket = socket

    def call(self):
        return self.socket.receive_data()
        
