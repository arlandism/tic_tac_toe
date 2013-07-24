import unittest
from socket_output import SocketOutput
from web_io_test_utils import MockSocket

class SocketOutputTests(unittest.TestCase):

    def test_it_receives_socket(self):
        mock = MockSocket()
        output_obj = SocketOutput(mock)

    def test_it_calls_socket_during_display(self):
        mock = MockSocket()
        output_obj = SocketOutput(mock)
        output_obj.display("stuff")
        self.assertEqual("stuff",mock.sent_stuff.pop())
