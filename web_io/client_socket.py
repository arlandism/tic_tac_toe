import socket

class Socket(object):

    def __init__(self,hostname="localhost",port=5000):
        self.port = port
        self.hostname = hostname
        self.is_connected = False
        self.socket = socket.socket()
        self.data = []

    def addr_info(self):
        return (self.hostname,self.port)

    def connect(self):
        self.socket.connect((self.hostname,self.port)) 
        self.is_connected = True

    def send_data(self,to_send):
        self.socket.send(to_send)

    def receive_data(self):
        self.data.append(self.socket.recv(4096)) 

    def connected(self):
        return self.is_connected

    def close(self):
        self.socket.close()
        self.is_connected = False 

