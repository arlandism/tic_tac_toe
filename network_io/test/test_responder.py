import unittest
import mock
from responder import Responder, MoveGenerator
from web_io_test_utils import MockTransmitter

class FakeMoveGenerator(object):

    def __init__(self, to_return,board=None):
        self.to_return = to_return
        self.argument_history = []

    def next_move(self, board_state):
        self.argument_history.append(board_state)
        return self.to_return

    def winner(self):
        pass

class ResponderTests(unittest.TestCase):

     def test_responds_got_something(self):
       transmitter = MockTransmitter([{"something":""}])
       responder = Responder(transmitter,mock.Mock())
       responder.respond()
       self.assertEqual(1,transmitter.times_receive_called)

     def test_respond_sent_something(self):
       transmitter = MockTransmitter(["stuff"])
       generator = FakeMoveGenerator([""])
       responder = Responder(transmitter,generator)
       responder.respond()
       self.assertEqual(2,transmitter.times_sent_called)

class ResponderIntegrationTests(unittest.TestCase):

    easy_win_possible = {1:"o", 2:"o", 4:"x", 7:"x"}
    bottom_row_win_possible = {7:"o", 8:"o"}

    #def test_returns_board_with_obvious_move(self):
    #    transmitter = mock.Mock()
    #    transmitter.receive = mock.MagicMock(return_value=self.easy_win_possible)
    #    minimax = mock.Mock()
    #    minimax.next_move = mock.MagicMock(return_value=3)
    #    generator = MoveGenerator(minimax=minimax)
    #    responder = Responder(transmitter,generator)
    #    responder.respond()
    #    transmitter.send.assert_called_with(3, "o")

    def test_response_with_best_move(self):
        transmitter = MockTransmitter([self.easy_win_possible])
        generator = FakeMoveGenerator(5)
        responder = Responder(transmitter,generator) 
        responder.respond()
        self.assertEqual(generator.to_return, 5)

    def test_calls_next_move_with_board_state(self):
        transmitter = MockTransmitter([self.easy_win_possible])
        generator = FakeMoveGenerator(5)
        responder = Responder(transmitter,generator) 
        responder.respond()
        self.assertGeneratorNextMoveCalledWith(generator,self.easy_win_possible)

    def assertGeneratorNextMoveCalledWith(self,generator,called_with):
        self.assertEqual(generator.argument_history[0], called_with)

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
