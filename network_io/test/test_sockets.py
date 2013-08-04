import unittest
import random
from server_socket import ServerSocket
from client_socket import Socket 
from json_transmitter import JsonTransmitter

class ClientInitTests(unittest.TestCase):

    def test_it_defaults_with_port_and_host(self):
        host, port = Socket().addr_info()
        self.assertEqual("localhost",host)
        self.assertEqual(5000,port)

    def test_it_can_be_initialized_with_other_addrs(self):
        socket = Socket('other_host',3000)
        host, port = socket.addr_info()
        self.assertEqual("other_host",host)
        self.assertEqual(3000,port)

class ConnectionTests(unittest.TestCase):

    def test_client_can_send_data(self):
        self.connect_client_and_build_connection_socket()
        self.client_socket.send_data("test data")
        self.assertEqual("test data",self.connection_socket.recv(1024))

    def test_server_can_send_data(self):
        self.connect_client_and_build_connection_socket()
        self.connection_socket.send("back at ya")
        self.client_socket.receive_data()
        self.assertEqual("back at ya", self.client_socket.data[0])

    def test_socket_knows_when_other_side_hangs_up(self):
        self.connect_client_and_build_connection_socket()
        self.assertTrue(self.client_socket.connected())
        self.connection_socket.send("")

    def setUp(self):
        valid_port = random.randrange(1024,65535)
        self.client_socket = Socket(port=valid_port)
        self.host, self.port = self.client_socket.addr_info()
        self.server_socket = self.setUpServerSocket(self.host,self.port)

    def tearDown(self):
        self.client_socket.close()
        self.server_socket.close()
        self.connection_socket.close()

    def connect_client_and_build_connection_socket(self):
        self.client_socket.connect()
        self.connection_socket = self.setUpConnectionSocket(self.server_socket)

    def setUpServerSocket(self,host,port):
        server_socket = ServerSocket(host,port)
        server_socket.initialize_and_listen_for_connections()
        return server_socket

    def setUpConnectionSocket(self,server_socket):
        return server_socket.accept_connection_and_return_socket()
