import socket

class ServerSocket(object):

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.socket = socket.socket()
        self.client = None

    def bind(self):
        self.socket.bind((self.host,self.port))

    def listen(self):
        self.socket.listen(1)

    def accept_connection_and_return_socket(self):
        client, addr = self.socket.accept()
        self.client = client
        return client

    def send(self,to_send):
        self.client.send(to_send) 

    def initialize_and_listen_for_connections(self):
        self.socket.bind((self.host,self.port))
        self.socket.listen(1)

    def close(self):
        self.socket.close()
