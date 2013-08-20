import unittest
import mock

from game.game import *
from game.base_board import BaseBoard
from game.test.test_utils import MockPlayer

from test.test_utils import FakePrinter,SimpleMockPrompter, MockUserInput

from players.ai import ImpossibleAI
from players.player import HumanPlayer

class GameRunTests(unittest.TestCase):

    def setUp(self):
        self.user_input = SimpleMockPrompter 
        self.player_one = mock.Mock()
        self.player_one.token = "x"
        self.player_two = mock.Mock()
        self.player_two.token = "o"

    def test_that_players_move(self):
        board = BaseBoard(3)
        self.player_one.next_move.side_effect = [1,2,3]
        self.player_two.next_move.side_effect = [4,5,6]
        game = Game(self.player_one, self.player_two, board)
        self.assertEqual(self.player_one,game.current_player)
        game.run()
        self.assertEqual(self.player_two,game.current_player)
        self.player_one.next_move.assert_called_with(board)
        self.player_two.next_move.assert_called_with(board)

    def test_that_players_dont_move_when_game_over(self):
        board = BaseBoard(3)
        board.set_state({1:"x",2:"o",3:"x",
			                   4:"o",5:"x",6:"o",
				                 7:"x",8:"o",9:"x"})
        game = Game(self.player_one,self.player_two,board)
        game.run()
        self.assertFalse(self.player_one.next_move.called)
        self.assertFalse(self.player_two.next_move.called)

    def test_that_board_is_printed_when_game_is_over(self):
        self.player_one.next_move = mock.MagicMock(return_value=1)
        self.player_two.next_move = mock.MagicMock(return_value=3)
        board = BaseBoard(3)
        board.set_state({1:"x",2:"x",3:"x"})
        fake_printer = FakePrinter()
        game = Game(self.player_one,self.player_two,board,prompter=fake_printer)
        game.run()
        self.assertEqual(True,game.__over__())
        expected_string = game.board.__str__()
        self.assertTrue(expected_string in fake_printer.history)

    def test_that_game_prints_board_after_each_set_of_rounds(self):
        self.player_one.next_move.side_effect = [1,2,3]
        self.player_two.next_move.side_effect = [4,5]
        fake_printer = FakePrinter()
        game = Game(self.player_one,self.player_two,prompter=fake_printer)
        game.run()
        # Two sets of rounds plus final print
        self.assertTrue(len(fake_printer.history) >= 6)

    def test_that_game_displays_winner(self):
        self.player_one.next_move.side_effect = [1,2,3]
        self.player_two.next_move.side_effect = [4,5]
        fake_printer = FakePrinter()
        game = Game(self.player_one,self.player_two,prompter=fake_printer)
        game.run()
        self.assertEqual("x",game.board.winner())
        self.assertTrue("x wins" in fake_printer.history)

    def test_that_game_prints_tie(self):
        fake_player_one = MockPlayer("x",self.user_input([1,6,8,7,5]))
        fake_player_two = MockPlayer("o",self.user_input([2,3,4,9]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,prompter=fake_printer)
        game.run()
        self.assertEqual(None,game.board.winner())
        self.assertTrue("It's a tie." in fake_printer.history)

    def create_fake_input_objects(self,input_list_one,input_list_two):
        input_one = self.user_input(input_list_one)
        input_two = self.user_input(input_list_two)
        return input_one, input_two

    def test_that_round_doesnt_run_when_game_over(self):
        fake_player_one = MockPlayer("x",self.user_input([1,2,3]))
        fake_player_two = MockPlayer("o",self.user_input([4]))
        game = Game(fake_player_one,fake_player_two)
        for i in range(1,4):
            game.board.make_move(i,"o")
        self.assertTrue(game.board.over())
        game.run()
        times_game_prompts_player_one = fake_player_one.prompter.times_called
        self.assertEqual(0,times_game_prompts_player_one)
 
    def test_that_board_isnt_printed_when_game_over(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",self.user_input([1]))
        fake_player_two = MockPlayer("o",self.user_input([2]))
        game = Game(fake_player_one,fake_player_two,prompter=fake_printer)
        game.__print_board_if_game_not_over__()
        #Game gets printed once when game over
        self.assertEqual(1,len(fake_printer.history))

    def test_that_board_is_printed_when_game_not_over(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",self.user_input([1,2,3]))
        fake_player_two = MockPlayer("o",self.user_input([4,5]))
        game = Game(fake_player_one,fake_player_two,prompter=fake_printer)
        game.run()
        self.assertTrue(len(fake_printer.history) >= 6)

    def assertInputObjectsCalled(self,input_obj_one,input_obj_two):
	      self.assertTrue(input_obj_one.times_called >= 1 and
			  input_obj_two.times_called >= 1)

    def assertInputObjectsNotCalled(self,input_obj_one,input_obj_two):
        self.assertTrue(input_obj_one.times_called == 0 and
			  input_obj_two.times_called == 0)

    def create_fake_players(self,*input_objs):
        input_object_one,input_object_two = input_objs
        player_one = MockPlayer("x",input_object_one)
        player_two = MockPlayer("o",input_object_two)
        return player_one, player_two

