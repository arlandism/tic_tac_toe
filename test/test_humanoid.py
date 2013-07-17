import unittest

from humanoid import Humanoid
from base_board import BaseBoard
from test_utils import MockUserInput, FakePrinter, FakeMinimax

class HumanoidNextMoveTests(unittest.TestCase):

    def setUp(self):
        self.board = BaseBoard(3)

    def tearDown(self):
        self.board.board_state = {}

    def test_first_move_is_human(self):
        mock = MockUserInput([1])      
        player = Humanoid("x",input_object=mock)
        self.assertEqual(1,player.next_move(self.board))
       
    def test_second_move_is_human(self):
        mock = MockUserInput([1,2])
        player = Humanoid("x",input_object=mock)
        self.assertEqual(1,player.next_move(self.board))
        self.assertEqual(2,player.next_move(self.board))

    def test_gets_minimax(self):
        player = Humanoid("x",input_object=MockUserInput([1,2,5]),
        minimax=FakeMinimax())
        for i in range(3):
            player.next_move(self.board)
        self.assertEqual("next move", player.next_move(self.board))

    def test_third_move_is_ai(self):
        mock = MockUserInput([1,7])
        player = Humanoid("x",input_object=mock)
        self.board.board_state = {4:"o", 5:"o"}
        self.assertEqual(1,player.next_move(self.board))

        self.board.board_state = {1:"x", 4:"o", 5:"o"}
        self.assertEqual(7,player.next_move(self.board))

        self.board.board_state = {1:"x", 4:"o", 5:"o", 7:"x"}
        self.assertEqual(6,player.next_move(self.board))
                         
    def test_for_prompts(self):
        mock = MockUserInput([1])
        fake_printer = FakePrinter()
        humanoid = Humanoid("x",mock,fake_printer)
        humanoid.next_move(BaseBoard(3))
        self.assertTrue("X's turn" in fake_printer.history_string())
        self.assertTrue("Available moves are " in fake_printer.history_string())
        self.assertTrue("X moves to 1" in fake_printer.history_string())
        self.assertTrue("Please select a move: " in fake_printer.history_string())
