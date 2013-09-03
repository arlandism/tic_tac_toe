import unittest
import mock

from move_generator import MoveGenerator, MustBeInt

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

    def test_handler_raises_error_with_non_int_difficulties(self):
        board_state = {1:"x",2:"x",5:"o"}
        difficulty = "supercalifragilisticexpialidocious"
        generator = MoveGenerator()
        self.assertRaises(MustBeInt,generator.next_move,board_state,difficulty)

    def test_winner_of_returns_correct_winner(self):
        board_state = {1:"x",2:"x",3:"x"}
        self.assertEqual("x",MoveGenerator().winner_of(board_state))
