import unittest
import mock
from responder import Responder, MoveGenerator, ResponseHandler, MustBeInt

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

class ResponseHandlerTests(unittest.TestCase):
    
    def test_response_delegates_to_move_generator(self):
        data = {"board": {1:"x",2:"x",5:"o"}}
        handler = ResponseHandler(MoveGenerator())
        response = handler.response(data)
        self.assertEqual(3,response["move"])
        self.assertEqual(None,response["winner"])

class MoveGeneratorTests(unittest.TestCase):

    def test_board_winner_called(self):
        board = mock.Mock()
        board.winner = mock.MagicMock(return_value="o")
        generator = MoveGenerator(board)
        self.assertEqual("o",generator.winner())
        board.winner.assert_called_once_with()

    def test_minimax_next_move_called(self):
        board = {1:"o",2:"o"}
        generator = MoveGenerator()
        self.assertEqual(3,generator.next_move(board))

    def test_generator_calls_winner_when_expected(self):
        generator = MoveGenerator()
        board_state = {9:"x", 5:"o", 6:"x"}
        self.assertEqual(3, generator.next_move(board_state))
        self.assertEqual(None,generator.winner())

    def test_handler_defaults_with_non_int_difficulties(self):
        board_state = {1:"x",2:"x",5:"o"}
        difficulty = "supercalifragilisticexpialidocious"
        generator = MoveGenerator()
        self.assertRaises(MustBeInt,generator.next_move,board_state,difficulty)

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
        self.assertEqual(None, transmitter.send.call_args[0][0]["winner"])
