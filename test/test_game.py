import unittest
from game import *
from board import *
from ai import ImpossibleAI
from easy_ai import EasyAI
from test_utils import FakePrinter, MockUserInput, MockPlayer
from player import HumanPlayer
from playerinput import InputValidator
from fours_board import FourByFourBoard

class GameRunTests(unittest.TestCase):

    def test_that_players_move(self):
	player_one_input,player_two_input = self.create_fake_input_objects([1,2,3],[4,5,6])
	fake_player_one,fake_player_two = self.create_fake_players(player_one_input,player_two_input)
	game = Game(fake_player_one, fake_player_two)
	game.run()
	self.assertInputObjectsCalled(player_one_input,player_two_input)

    def test_that_players_dont_move_when_game_over(self):
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2]))
        game = Game(fake_player_one,fake_player_two)
	game.board.board_state = {1:"x",2:"o",3:"x",
			              4:"o",5:"x",6:"o",
				      7:"x",8:"o",9:"x"}
        self.assertEqual(True,game.board.over())
        game.run()
	self.assertInputObjectsNotCalled(fake_player_one.input_object,
			                 fake_player_two.input_object)

    def test_that_board_is_printed_when_game_is_over(self):
	fake_player_one = MockPlayer("x",MockUserInput([1]))
	fake_player_two = MockPlayer("o",MockUserInput([2]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
	game.board.board_state = {1:"x",2:"x",3:"x"}
        game.run()
        self.assertEqual(True,game.__over__())
        expected_string = ("\n%(1)3s|%(2)3s|%(3)3s\n------------" +
                           "\n%(4)3s|%(5)3s|%(6)3s\n------------" +
                           "\n%(7)3s|%(8)3s|%(9)3s") % game.board.generate_layout()
        self.assertTrue(expected_string in fake_printer.history)

    def test_that_game_prints_board_after_each_set_of_rounds(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.run()
        # Two sets of rounds plus final print
        self.assertTrue(len(fake_printer.history) >= 6)

    def test_that_game_displays_winner(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.run()
        self.assertEqual("x",game.board.winner())
        self.assertTrue("x wins" in fake_printer.history)

    def test_that_game_prints_tie(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,6,8,7,5]))
        fake_player_two = MockPlayer("o",MockUserInput([2,3,4,9]))
        fake_printer = FakePrinter()
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
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
	game = Game(player_one,player_two,board=FourByFourBoard())
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
	input_one = MockUserInput(input_list_one)
	input_two = MockUserInput(input_list_two)
	return input_one, input_two

class GameRoundTests(unittest.TestCase):

    def test_that_round_doesnt_run_when_game_over(self):
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4]))
        game = Game(fake_player_one,fake_player_two)
        for i in range(1,4):
            game.board.make_move(i,"o")
        self.assertTrue(game.board.over())
	game.run()
        times_game_prompts_player_one = fake_player_one.input_object.times_called
        self.assertEqual(0,times_game_prompts_player_one)
 
    def test_that_sample_board_shown(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.run()
        example_board = ("\n1|2|3\n-------" +
                          "\n4|5|6\n-------" +
                          "\n7|8|9\n")
        self.assertTrue(example_board in fake_printer.history)


class GamePrintBoardIfNotOverTests(unittest.TestCase):

    def test_that_board_isnt_printed_when_game_over(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",MockUserInput([1]))
        fake_player_two = MockPlayer("o",MockUserInput([2]))
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.__print_board_if_game_not_over__()
        #Game gets printed once when game over
        self.assertEqual(1,len(fake_printer.history))

    def test_that_board_is_printed_when_game_not_over(self):
        fake_printer = FakePrinter()
        fake_player_one = MockPlayer("x",MockUserInput([1,2,3]))
        fake_player_two = MockPlayer("o",MockUserInput([4,5]))
        game = Game(fake_player_one,fake_player_two,display_object=fake_printer)
        game.run()
        self.assertTrue(len(fake_printer.history) >= 6)

class GameMoveTests(unittest.TestCase):

    def test_that_move_works_with_easy_ai(self):
        computer = EasyAI("o")
        game = Game(HumanPlayer("x"),computer)
        game.__move__(computer.next_move(game.board),computer)
        empty_board = {}
        self.assertTrue(game.board.state() != empty_board)
