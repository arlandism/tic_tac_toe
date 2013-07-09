import unittest
from board import *

class BoardInitTests(unittest.TestCase):

    def test_if_new_board_is_empty_dict(self):
        self.assertEqual(dict(),Board().board_state)

class Board__Str__Tests(unittest.TestCase):

    def test_if_game_returns_no_pieces(self):
        board = Board()
        NOT_FOUND = -1
        self.assertEqual(NOT_FOUND,board.__str__().find('x'))
        self.assertEqual(NOT_FOUND,board.__str__().find('o'))

    def test_if_board_returns_correct_layout(self):
        board = Board()
        board.make_move(1,'x')
        self.assertEqual(1,board.__str__().count('x'))

class BoardRowTests(unittest.TestCase):
        
    def test_rows(self):
        self.assertEqual([[1,2,3],[4,5,6],[7,8,9]],Board().rows())

class BoardStateTests(unittest.TestCase):

    def test_if_state_returns_empty_dict_with_no_moves(self):
        board = Board()
        self.assertEqual(dict(),board.state())

    def test_if_state_returns_correct_mappings(self):
        board = Board()
        board.make_move(1,'x')
        board.make_move(3,'o')
        self.assertEqual({1:'x',3:'o'},board.state())

class BoardMakeMoveTests(unittest.TestCase):

    def test_if_make_move_alters_board_state(self):
	board = Board()
	board.make_move(1,"x")
	self.assertEqual({1:"x"},board.state())

class BoardGameOverTests(unittest.TestCase):

    def test_if_game_over_returns_false_at_game_beginning(self):
        board = Board()
        self.assertEqual(False, board.over())

    def test_if_game_over_returns_true_when_board_is_full(self):
        board = Board()
	board.board_state = {1:"x",2:"x",3:"o",
			     4:"o",5:"x",6:"x",
			     7:"x",8:"o",9:"o"}
        self.assertEqual(True,board.over())

    def test_if_game_over_returns_true_when_there_is_winner(self):
        board = Board()
	board.board_state = {1:"x",2:"x",3:"x"}
        self.assertEqual(True,board.over())

    def test_if_game_over_returns_false_with_empty_square(self):
        board = Board()
	board.board_state = {1:"x",2:"o",3:"x",
			     4:"o",5:"x",7:"o",
			     8:"x"}
        self.assertEqual(False,board.over())

class BoardWinnerTests(unittest.TestCase):

    def test_if_winner_returns_none_with_blank_board(self):
        self.assertEqual(None,Board().winner())

    def test_if_winner_returns_none_with_no_win(self):
        board = Board()
        board.make_move(1,'x')
        self.assertEqual(None,board.winner())

    def test_if_winner_returns_token_with_win(self):
        board = Board()
	board.board_state = {1:"x",2:"x",3:"x"}
	self.assertEqual("x",board.winner())

    def test_winner_with_other_combo(self):
        board = Board()
	board.board_state = {1:"o",2:"o",3:"o"}
	self.assertEqual("o",board.winner())

    def test_if_winner_returns_none_with_full_board_no_win(self):
        board = Board()
	board.board_state = {1:"x",2:"o",3:"x",
			     4:"o",5:"o",6:"x",
			     7:"x",8:"x",9:"o"}
        self.assertEqual(None,board.winner())

    def test_that_winner_always_returns_token_or_none(self):
        board = Board()
	board.board_state = {1:"x",2:"x",3:"x"}
        self.assertEqual("x",board.winner())

        board.board_state = {1:"o",2:"o",3:"o"}
	self.assertEqual("o",board.winner())

        board.board_state = {}
        self.assertEqual(None,board.winner())


class BoardIsFullTests(unittest.TestCase):

    def test_is_full_on_empty_board(self):
        self.assertEqual(False, Board().is_full())

    def test_is_full_on_non_empty_board(self):
        board = Board()
        board.make_move(1,'x')
        self.assertEqual(False, board.is_full())

    def test_is_full_on_full_board(self):
        board = Board()
	board.board_state = {1:"x",2:"o",3:"x",
			     4:"x",5:"o",6:"x",
			     7:"o",8:"x",9:"o"}
        self.assertEqual(True, board.is_full())

class BoardAvailableMovesTests(unittest.TestCase):

    def test_if_available_moves_returns_range_ten(self):
        actual_available_moves = Board().available_moves()
        expected_available_moves = range(1,10)
        self.assertEqual(expected_available_moves, actual_available_moves)

    def test_available_moves_when_one_space_occupied(self):
        board = Board()
        board.make_move(1,'x')
        actual_available_moves = board.available_moves()
        expected_available_moves = range(2,10)
        self.assertEqual(expected_available_moves, actual_available_moves)

    def test_available_moves_when_all_spaces_occupied(self):
        board = Board()
	board.board_state = {1:"x",2:"o",3:"x",
			     4:"o",5:"x",6:"o",
			     7:"x",8:"o",9:"x"}
        available_moves = board.available_moves()
        self.assertEqual([], available_moves)

class BoardEraseMoveTests(unittest.TestCase):

    def test_if_reset_erases_move(self):
        board = Board()
        board.make_move(1,'x')
        board.erase_move(1)
        self.assertEqual({},board.board_state)
