import unittest
import mock
from responder import Responder
from response_handler import ResponseHandler
from move_generator import MoveGenerator, MustBeInt

class ResponderTests(unittest.TestCase):

    def setUp(self):
        self.transmitter = mock.Mock()
        self.transmitter.receive = mock.MagicMock(return_value={"board":{}})
        self.generator = mock.Mock()
 
    def test_responder_hands_what_it_got_from_receive_to_handler(self):
        self.transmitter.receive = mock.MagicMock(return_value="for the handler")
        handler = ResponseHandler(MoveGenerator())
        handler.response = mock.Mock()
        responder = Responder(self.transmitter,handler)
        responder.respond()
        handler.response.assert_called_with("for the handler")

    def test_responder_sends_what_it_got_from_handler(self):
        handler = ResponseHandler(mock.Mock())
        handler.response = mock.MagicMock(return_value="some stuff")
        responder = Responder(self.transmitter, handler)
        responder.respond()
        self.transmitter.send.assert_called_with("some stuff")

class IntegrationTests(unittest.TestCase):

    def test_integration_of_parts(self):
        DUMB_AI_DEPTH = 1
        data_from_transmitter_receive = {"board":{1:"x", 2:"x"},
                                         "depth":DUMB_AI_DEPTH}
        SMART_MOVE = 3
        transmitter = mock.Mock()
        transmitter.receive = mock.MagicMock(return_value=data_from_transmitter_receive)
        handler = ResponseHandler(MoveGenerator())
        responder = Responder(transmitter,handler)
        responder.respond()
        self.assertNotEqual(SMART_MOVE, transmitter.send.call_args[0][0]["move"])
        self.assertEqual(None, transmitter.send.call_args[0][0]["winner_after_ai_move"])
