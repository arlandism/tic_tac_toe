import unittest
import mock
from server_socket import ServerSocket

class ConnectionTests(unittest.TestCase):

    def test_server_accesses_its_clients_send_method(self):
        server = ServerSocket("localhost",5000) 
        server.client = mock.Mock()
        server.client.send = mock.MagicMock()
        server.send("Hello World!")
        server.client.send.assert_called_with("Hello World!")

    def test_accept_connection_delegates_to_its_socket(self):
        server = ServerSocket("localhost",5000) 
        server.socket = mock.Mock()
        server.socket.accept = mock.MagicMock(return_value=("client socket","address"))
        self.assertEqual("client socket", server.accept_connection_and_return_socket())

    def test_initialize_delegates_to_its_socket(self):
        server = ServerSocket("localhost",5000) 
        server.socket = mock.Mock()
        server.socket.bind = mock.MagicMock()
        server.socket.listen = mock.MagicMock()
        server.initialize_and_listen_for_connections()
        server.socket.bind.assert_called_with(("localhost",5000))
        self.assertEqual(1,server.socket.listen.call_count)
