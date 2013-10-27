import unittest
import mock
from response_thread import ResponseThread

class ResponseThreadTests(unittest.TestCase):
    
    def test_responder_respond_called(self):
        responder = mock.Mock()
        responder.respond = mock.MagicMock()
        thread = ResponseThread(responder)
        thread.run()
        responder.respond.assert_any_call()
