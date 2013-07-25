import unittest
import socket
import time
import random
from client_socket import Socket 

class ClientSocketTests(unittest.TestCase):

    def setUp(self):
        valid_port = random.randrange(1024,65535)
        self.socket = Socket(port=valid_port)

    def tearDown(self):
        self.socket.close()

    def test_it_defaults_with_port_and_host(self):
        host, port = Socket().addr_info()
        self.assertEqual("localhost",host)
        self.assertEqual(5000,port)

    def test_it_can_be_initialized_with_other_addrs(self):
        socket = Socket('other_host',3000)
        host, port = socket.addr_info()
        self.assertEqual("other_host",host)
        self.assertEqual(3000,port)
        self.close_active_sockets(socket)

    def test_it_can_send_data(self):
        host, port = self.socket.addr_info()
        server_socket = self.setUpServerSocket(host,port)
        self.socket.connect()
        server_connection_socket = server_socket.accept_connection_and_return_socket()
        self.socket.send_data("test data")
        self.assertEqual("test data",server_connection_socket.recv(1024))
        self.close_active_sockets(server_socket,server_connection_socket)

    def test_it_can_receive_data(self):
        host, port = self.socket.addr_info()
        server_socket = self.setUpServerSocket(host,port)
        self.socket.connect()
        server_connection_socket = server_socket.accept_connection_and_return_socket()
        server_connection_socket.send("back at ya")
        self.socket.receive_data()
        self.assertEqual("back at ya", self.socket.data[0])
        self.close_active_sockets(server_socket,server_connection_socket)

    def close_active_sockets(self,*sockets):
        for socket in sockets:
            socket.close()

    def setUpServerSocket(self,host,port):
        server_socket = ServerSocket(host,port)
        server_socket.initialize_and_listen_for_connections()
        return server_socket

class ServerSocket(object):

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.socket = socket.socket()

    def bind(self):
        self.socket.bind((self.host,self.port))

    def listen(self):
        self.socket.listen(1)

    def accept_connection_and_return_socket(self):
        client, addr = self.socket.accept()
        return client

    def initialize_and_listen_for_connections(self):
        self.socket.bind((self.host,self.port))
        self.socket.listen(1)

    def close(self):
        self.socket.close()
