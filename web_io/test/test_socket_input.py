import unittest
from socket_input import SocketInput

class SocketInputTests(unittest.TestCase):

    def test_it_gets_a_socket(self):
        mock = MockSocket()
        input_obj = SocketInput(mock)

    def test_calls_sockets_send_data_meth(self):
        mock = MockSocket()
        input_obj = SocketInput(mock)
        self.assertEqual('got some stuff', input_obj.call())


class MockSocket(object):

  def send_data(self):
      return 'some stuff'

  def receive_data(self):
      return 'got some stuff'
