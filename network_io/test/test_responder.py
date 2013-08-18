import unittest
import mock
from responder import Responder, MoveGenerator

class ResponderTests(unittest.TestCase):

    def setUp(self):
        self.transmitter = mock.Mock()
        self.transmitter.receive = mock.MagicMock(return_value={"board":{}})
        self.generator = mock.Mock()
 
    def test_responder_hands_what_it_got_from_receive_to_generator(self):
        self.transmitter.receive = mock.MagicMock(return_value="for the generator")
        responder = Responder(self.transmitter,self.generator)
        responder.respond()
        self.generator.response.assert_called_with("for the generator")

    def test_responder_sends_what_it_got_from_move_generator(self):
        generator = MoveGenerator()
        generator.response = mock.MagicMock(return_value="some stuff")
        responder = Responder(self.transmitter, generator)
        responder.respond()
        self.transmitter.send.assert_called_with("some stuff")
    
class MoveGeneratorTests(unittest.TestCase):

    def test_board_winner_called(self):
        board = mock.Mock()
        board.winner = mock.MagicMock(return_value="o")
        generator = MoveGenerator(board)
        self.assertEqual("o",generator.winner())
        board.winner.assert_called_once_with()

    def test_minimax_next_move_called(self):
        minimax = mock.Mock()
        minimax.next_move = mock.MagicMock(return_value=3)
        generator = MoveGenerator(minimax=minimax)
        self.assertEqual(3,generator.next_move({}))
        self.assertTrue(minimax.next_move.called)

    def test_minimax_next_move_called_with_given_board(self):
        board = mock.Mock()
        minimax = mock.Mock()
        generator = MoveGenerator(board,minimax)
        generator.next_move({})
        minimax.next_move.assert_called_with(board)

    def test_move_generator_delegates_to_ai(self):
        fake_ai = mock.Mock()
        fake_ai.next_move = mock.MagicMock(return_value=99)
        generator = MoveGenerator(minimax=fake_ai)
        actual_move = generator.next_move({})
        self.assertEqual(99,actual_move)

    def test_generator_calls_winner_when_expected(self):
        generator = MoveGenerator()
        board_state = {9:"x", 5:"o", 6:"x"}
        self.assertEqual(3, generator.next_move(board_state))
        self.assertEqual(None,generator.winner())

    def test_generator_with_buggy_move_sequence(self):
        generator = MoveGenerator()
        board_state = {9:"x", 5:"o", 6:"x"}
        self.assertEqual(3,generator.next_move(board_state))
