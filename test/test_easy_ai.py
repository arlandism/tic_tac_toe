import unittest

from game import Game
from board import Board
from easy_ai import EasyAI
from ai import ImpossibleAI
from test_utils import FakePrinter,FakeMinimax

class EasyAiTests(unittest.TestCase):

    def test_that_it_doesnt_block(self):
	board = Board()
	computer = EasyAI("x")
	board.board_state = {1:"o",2:"o",4:"x"}
	self.assertTrue(computer.next_move(board) != 3)

    def test_that_it_wont_beat_impossible_ai(self):
	board = Board()
	computer = EasyAI("x")
	computer_two = ImpossibleAI("o")
	game = Game(computer,computer_two)
	game.run()
	self.assertTrue(game.board.winner() != "x")

    def test_for_prompts(self):
	fake_printer = FakePrinter()
	computer = EasyAI("x",fake_printer)
	board = Board()
	board.board_state = {1:"x",2:"o",3:"x",
			     4:"o",5:"o",6:"x",
			           8:"x", 9:"o"}
	computer.next_move(board)
        NOT_FOUND = -1
	history = "".join(fake_printer.history)
	status = history.find("X moves to 7")
	self.assertNotEqual(NOT_FOUND,status)

        status = history.find(computer.token.capitalize() + "'s turn")
	self.assertNotEqual(NOT_FOUND,status)

    def test_it_receives_minimax(self):
        computer = EasyAI("x")
	self.assertEqual("next move",computer.next_move(Board(),FakeMinimax()))

