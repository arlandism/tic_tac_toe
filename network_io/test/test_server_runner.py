import unittest
import server_runner
from web_io_test_utils import MockServer

class ServerRunnerTests(unittest.TestCase):

    def setUp(self):
        self.mock = MockServer("localhost",9000)
        self.runner = server_runner.ServerRunner(self.mock)

    def test_runner_starts_the_server(self):
        self.runner.start_server()
        self.assertTrue(self.mock.started)

    def test_runner_calls_server_accept_connection(self):
        self.runner.start_server()
        self.runner.accept_connections()
        self.assertTrue(self.mock.accept_method_called)

    def test_runner_cant_accept_connections_when_server_off(self):
        self.assertRaises(server_runner.ServerOffException,self.runner.accept_connections)
