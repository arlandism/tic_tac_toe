import unittest

from game.base_board import BaseBoard

class BaseBoardTests(unittest.TestCase):

    def test_if_new_board_is_empty_dict(self):
        self.assertEqual(dict(),BaseBoard(3).state())

    def test_state_returns_only_non_junk(self):
        garbage_state = {0:"", 5:"o", 6:"x", 9:"x"}
        board = BaseBoard(3)
        board.board_state = garbage_state
        self.assertEqual( {5:"o", 6:"x", 9:"x"}, board.state())

    def test_set_state(self):
        board = BaseBoard(3)
        self.assertEqual({},board.state())
        board.set_state({1:"x"})
        self.assertEqual({1:"x"},board.state())

    def test_set_state_doesnt_alter_original_object(self):
        board = BaseBoard(3)
        original_state = {"state":"stuff"}
        board.set_state(original_state)
        board.make_move(2,"x")
        self.assertEqual({"state":"stuff"}, original_state)

    def test_make_move(self):
        board = BaseBoard(3)
        board.make_move(1,"x")
        self.assertEqual({1:"x"},board.state())

class BaseBoardWinnerTests(unittest.TestCase):

    def test_winner(self):
        board = BaseBoard(base=3)
        board.board_state = {1:"me",2:"me",3:"me"}
        self.assertEqual("me",board.winner())

    def test_winner_with_twos_board(self):
        board = BaseBoard(base=2)
        board.board_state = {1:"you",4:"you"}
        self.assertEqual("you",board.winner())

    def test_winner_with_no_win(self):
        board = BaseBoard(base=3)
        board.board_state = {1:"x",2:"x",3:"o"}
        self.assertEqual(None,board.winner())

    def test_winner_with_tie(self):
        board = BaseBoard(base=3)
        board.board_state = {1:"x",2:"x",3:"o",
                             4:"o",5:"x",6:"x",
                             7:"x",8:"o",9:"o"}
        self.assertTrue(board.is_full())
        self.assertEqual(None,board.winner())

class BaseBoardFullTests(unittest.TestCase):

    def test_full_on_full_board(self):
        board = BaseBoard(base=3)
        board.board_state = {1:"o",2:"o",3:"x",
                             4:"x",5:"x",6:"o",
                             7:"o",8:"o",9:"x"}
        self.assertTrue(board.is_full())

    def test_full_with_empty_board(self):
        self.assertFalse(BaseBoard(3).is_full())

    def test_full_with_win(self):
        board = BaseBoard(3)
        board.board_state = {1:"x",2:"x",3:"x"}
        self.assertFalse(board.is_full())

    def test_full_with_fours_board(self):
        board = BaseBoard(4)
        board.board_state = {1:"o",2:"o",3:"x",
                             4:"x",5:"x",6:"o",
                             7:"o",8:"o",9:"x"}
        self.assertFalse(board.is_full())

class BaseBoardAvailableMovesTests(unittest.TestCase):

    def test_available_moves_with_fours_board(self):
        self.assertEqual(range(1,17),BaseBoard(base=4).available_moves())

    def test_available_moves_with_threes_board(self):
        self.assertEqual(range(1,10),BaseBoard(3).available_moves())

    def test_available_moves_with_full_board(self):
        board = BaseBoard(3)
        board.board_state = {1:"o",2:"o",3:"x",
                             4:"x",5:"x",6:"o",
                             7:"o",8:"o",9:"x"}
        self.assertEqual([],board.available_moves())

    def test_available_moves_with_win_board(self):
        board = BaseBoard(3)
        board.board_state = {1:"o",2:"o",3:"o"}
        # Board assumes available moves not called when game over
        self.assertEqual(range(4,10),board.available_moves())

    def test_available_moves_with_partial_board(self):
        board = BaseBoard(3)
        board.board_state = {1:"x",5:"o"}
        self.assertEqual(range(2,5)+range(6,10),board.available_moves())

class BoardEraseMoveTests(unittest.TestCase):

    def test_erase_move(self):
        board = BaseBoard(base=2)
        board.make_move(3,"x")
        board.erase_move(3)
        self.assertEqual({},board.state())

class BaseBoardOverTests(unittest.TestCase):

    def test_over_with_empty_board(self):
        self.assertFalse(BaseBoard(3).over())

    def test_over_with_non_full_board(self):
        board = BaseBoard(3)
        board.board_state = {1:"x", 2:"o"}
        self.assertFalse(board.over())

    def test_over_with_win(self):
        self.assertFalse(BaseBoard(base=3).over())
        board = BaseBoard(base=3)
        board.board_state = {1:"x",2:"x",3:"x"}
        self.assertTrue(board.over())

    def test_over_with_full_threes_board(self):
        board = BaseBoard(3)
        board.board_state = {1:"x",2:"x",3:"o",
			                       4:"o",5:"x",6:"x",
			                       7:"x",8:"o",9:"o"}
        self.assertEqual(True,board.over())

    def test_over_with_full_fours_board(self):
        board = BaseBoard(4)
        board.board_state = {1:"o",2:"x",3:"x",4:"o",
                             5:"x",6:"o",7:"o",8:"x",
                             9:"x",10:"o",11:"o",12:"x",
                             13:"x",14:"x",15:"o",16:"x"}
        self.assertFalse(board.winner())
        self.assertTrue(board.over())

class ExampleBoardTests(unittest.TestCase):

    def test_example_board(self):
        example_board = (" 1  2  3 \n--------- 4  5  6 \n--------- 7  8  9")
