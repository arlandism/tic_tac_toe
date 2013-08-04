import unittest
from game.game import *
from game.base_board import BaseBoard
from game.ai import ImpossibleAI
from game.test.test_utils import MockPlayer
from test.test_utils import FakePrinter,SimpleMockPrompter, MockUserInput
from game.player import HumanPlayer
from io.playerinput import InputValidator

class GameRunTests(unittest.TestCase):

    def setUp(self):
        self.user_input = SimpleMockPrompter 

    def test_that_players_move(self):
        player_one_input,player_two_input = self.create_fake_input_objects([1,2,3],[4,5,6])
        fake_player_one,fake_player_two = self.create_fake_players(player_one_input,player_two_input)
        game = Game(fake_player_one, fake_player_two)
        game.run()
        self.assertInputObjectsCalled(player_one_input,player_two_input)

    def test_that_players_dont_move_when_game_over(self):
        fake_player_one = MockPlayer("x",self.user_input([1]))
        fake_player_two = MockPlayer("o",self.user_input([2]))
        game = Game(fake_player_one,fake_player_two)
        game.board.board_state = {1:"x",2:"o",3:"x",
			                            4:"o",5:"x",6:"o",
				                          7:"x",8:"o",9:"x"}
        self.assertEqual(True,game.board.over())
        game.run()
        self.assertInputObjectsNotCalled(fake_player_one.prompter,
			                                   fake_player_two.prompter)

    def test_that_board_is_printed_when_game_is_over(self):
        fake_player_one = MockPlayer("x",self.user_input([1]))
        fake_player_two = MockPlayer("o",self.user_input([2]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,prompter=fake_printer)
        game.board.board_state = {1:"x",2:"x",3:"x"}
        game.run()
        self.assertEqual(True,game.__over__())
        expected_string = game.board.__str__()
        self.assertTrue(expected_string in fake_printer.history)

    def test_that_game_prints_board_after_each_set_of_rounds(self):
        fake_player_one = MockPlayer("x",self.user_input([1,2,3]))
        fake_player_two = MockPlayer("o",self.user_input([4,5]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,prompter=fake_printer)
        game.run()
        # Two sets of rounds plus final print
        self.assertTrue(len(fake_printer.history) >= 6)

    def test_that_game_displays_winner(self):
        fake_player_one = MockPlayer("x",self.user_input([1,2,3]))
        fake_player_two = MockPlayer("o",self.user_input([4,5]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,prompter=fake_printer)
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

    def test_that_current_player_var_alternates(self):
        input_one,input_two = self.create_fake_input_objects([1,2,3],[4,5,6])
        player_one,player_two = self.create_fake_players(input_one,input_two)
        game = Game(player_one,player_two)
        #First player is x
        self.assertEqual("x",game.current_player.token)
        game.run()
        self.assertEqual("o",game.current_player.token)

    def test_flow_with_fours_board(self):
        input_one,input_two = self.create_fake_input_objects([9,10,11,12],[16,7,3,1])
        player_one,player_two = self.create_fake_players(input_one,input_two)
        game = Game(player_one,player_two,board=BaseBoard(4))
        game.run()
        self.assertTrue(game.board.over())

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

