import unittest
import mock
from responder import Responder, MoveGenerator

class ResponderTests(unittest.TestCase):

    def test_responds_got_something(self):
        transmitter = mock.Mock()
        transmitter.receive = mock.MagicMock()
        responder = Responder(transmitter,mock.Mock())
        responder.respond()
        self.assertEqual(1,transmitter.receive.call_count)

    def test_respond_sent_something(self):
        transmitter = mock.Mock()
        transmitter.send = mock.MagicMock()
        generator = mock.Mock()
        responder = Responder(transmitter,generator)
        responder.respond()
        self.assertEqual(2,transmitter.send.call_count)

    def test_respond_sends_next_move_from_generator(self):
        transmitter = mock.Mock()
        generator = mock.Mock()
        generator.winner = mock.MagicMock(return_value=None)
        generator.next_move = mock.MagicMock(return_value=3)
        responder = Responder(transmitter,generator)
        responder.respond() 
        transmitter.send.assert_any_call(3)
         
    def test_respond_sends_generator_winner(self):
        transmitter = mock.Mock() 
        generator = mock.Mock()
        generator.winner = mock.MagicMock(return_value="x")
        responder = Responder(transmitter, generator)
        responder.respond()
        transmitter.send.assert_called_with("x") 

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
