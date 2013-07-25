import unittest
import socket
from client_socket import Socket 

class ClientSocketTests(unittest.TestCase):

    def setUp(self):
        self.socket = Socket()

    def tearDown(self):
        self.socket.close()

    def test_it_defaults_with_port_and_host(self):
        host, port = self.socket.addr_info()
        self.assertEqual("localhost",host)
        self.assertEqual(5000,port)

    def test_it_can_be_initialized_with_other_addrs(self):
        socket = Socket('other_host',3000)
        host, port = socket.addr_info()
        self.assertEqual("other_host",host)
        self.assertEqual(3000,port)

    def test_it_can_connect(self):
        HOST = "localhost"
        PORT = 34000
        socket = Socket(HOST,PORT)
        read_socket = self.setUpServerSocket(HOST,PORT)
        socket.connect()
        server_client = read_socket.accept_connection()
        socket.send_data("test data")
        self.assertEqual("test data",server_client.recv(1024))
        self.assertTrue(socket.connected())
        self.close_active_sockets(socket,server_client,read_socket)

    def test_it_knows_when_connected(self):
        self.assertFalse(self.socket.connected())

    def test_it_can_receive(self):
        server_socket = self.setUpServerSocket("localhost",5000)
        self.socket.connect()
        server_client = server_socket.accept_connection()
        server_client.send("back at ya")
        self.socket.receive_data()
        self.assertEqual("back at ya", self.socket.data[0])
        server_socket.close()
        server_client.close()

    def close_active_sockets(self,*sockets):
        for socket in sockets:
            socket.close()

    def setUpServerSocket(self,host,port):
        read_socket = ServerSocket(host,port) 
        read_socket.bind()
        read_socket.listen()
        return read_socket

class ServerSocket(object):

    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.socket = socket.socket()

    def bind(self):
        self.socket.bind((self.host,self.port))

    def listen(self):
        self.socket.listen(1)

    def accept_connection(self):
        client, addr = self.socket.accept()
        return client

    def close(self):
        self.socket.close()
