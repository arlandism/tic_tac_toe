import unittest
from user_interface import *
from test_utils import *

class UserInterfaceGameSetupTests(unittest.TestCase):

    def return_prompts(self):
        prompt_one = ("Would you like to play against an easy or impossible ai: ") 
        prompt_two = ( "(1) Human vs AI\n" +
                       "(2) Human vs Human\n" +
                       "(3) AI vs AI\n" +
                       "(4) Humanoid vs AI")
        prompt_four = "Would you like to play as x or o: "
        prompt_three = "Would you like to move first or second (1,2): "
	return prompt_one,prompt_two,prompt_three,prompt_four

    def test_for_scenario_one_prompts(self):
	scenario = 1
	prompts = self.return_prompts()
	self.assert_prompts_present(scenario,*prompts)

    def test_scenario_four_prompts(self):
	scenario = 4
	prompts = self.return_prompts()
	self.assert_prompts_present(scenario,*prompts)

    def assert_prompts_present(self,scenario_number,*prompts):
	dummy_input = [scenario_number,1,"x","easy"]
	mock = MockUserInput(dummy_input)
        fake_printer = FakePrinter()
	ui = UserInterface(mock,fake_printer)
	ui.game_setup()
	history_string = " ".join(fake_printer.history)
	for prompt in prompts:
	    self.assertTrue(prompt in history_string)

    def call_game_setup_with_input_list(self,input_list):
	fake_printer = FakePrinter()
	mock = MockUserInput(input_list)
	ui = UserInterface(mock,fake_printer)
	return ui.game_setup()

class UserInterfaceShowFlaggedPromptsTests(unittest.TestCase):

    def test_that_appropriate_prompts_shown(self):
        mock = MockUserInput([3,"easy"])
	fake_printer = FakePrinter()
	ui = UserInterface(mock,fake_printer)
	ui.game_setup()
	# Prompt for choosing scenario is only necessary prompt
	prompts_necessary_for_scenario_three = 2
	printed_strings = len(fake_printer.history)
	self.assertEqual(printed_strings,prompts_necessary_for_scenario_three)

	mock = MockUserInput([2])
	fake_printer = FakePrinter()
	ui = UserInterface(mock,fake_printer)
	ui.game_setup()
	prompts_necessary_for_scenario_two = 1
	printed_strings = len(fake_printer.history)
	self.assertEqual(printed_strings,prompts_necessary_for_scenario_two)

        
