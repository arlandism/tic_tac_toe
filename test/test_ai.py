import unittest

from board import Board
from test_utils import FakePrinter, FakeMinimax

from ai import *

class AiNextMoveTests(unittest.TestCase):

    def test_if_ai_chooses_corner(self):
        computer = ImpossibleAI('o')
        game_board = Board()
        actual_move = computer.next_move(game_board)
        corners = (1,3,5,7,9)
        self.assertTrue(actual_move in corners)

    def test_if_ai_chooses_winning_move_with_threat(self):
        computer = ImpossibleAI('o')
        game_board = Board()
        game_board.make_move(1,'o')
        game_board.make_move(4,'x')
        game_board.make_move(5,'x')
        game_board.make_move(2,'o')
        computer_move = computer.next_move(game_board)
        self.assertEqual(3,computer_move)

    def test_ai_move_defense(self):
        board = Board()
        computer = ImpossibleAI("o")
        board.make_move(1,'o')
        board.make_move(5,'x')
        board.make_move(9,'x')
        move = computer.next_move(board)
        self.assertTrue(move in (3,7))

    def test_ai_goes_for_fastest_win(self):
	board = Board()
	computer = ImpossibleAI("x")
	board.make_move(1,"x")
	board.make_move(2,"x")
	move = computer.next_move(board)
	self.assertEqual(3,move)

    def test_for_prompts(self):
        fake_printer = FakePrinter()
	computer = ImpossibleAI("x",fake_printer)
	board = Board()
	board.board_state = {1:"x",2:"x"}
	computer.next_move(board)
	history_string = "".join(fake_printer.history)
	NOT_FOUND = -1
	status = history_string.find("X's turn")
	self.assertNotEqual(NOT_FOUND,status)
	
	status = history_string.find("x moves to 3")
	self.assertNotEqual(NOT_FOUND,status)

    def test_minimax_gets_called(self):
        computer = ImpossibleAI("x")
        fake_minimax = FakeMinimax() 
	self.assertEqual("next move",computer.next_move(Board(),fake_minimax))

