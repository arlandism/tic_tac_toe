
class SocketOutput(object):
 
    def __init__(self,socket):
        self.socket = socket

    def display(self,x):
        self.socket.send_data(x)
