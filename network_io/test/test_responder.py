import unittest
import mock
from responder import Responder, MoveGenerator, ResponseHandler

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

class IntegrationTests(unittest.TestCase):

    def test_ai_gets_instantiated_with_correct_depth(self):
        data = {"board":{1:"x", 2:"x"},
                "depth":1}
        handler = ResponseHandler(MoveGenerator())
        response = handler.response(data)
        self.assertNotEqual(3, response["move"])
