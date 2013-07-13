import unittest

from user_interface import *
from test_utils import *

class MockScenarioSelector(object):

    def __init__(self,user_input,display_object):
        self.user_input = user_input
	self.display_object = display_object
        self.display_object.display("Mock Selector Called!")
	self.mapping = {"give me a fake scenario":MockScenario}
	self.scenario = self.mapping[user_input.call()]

    def scenario_prompts(self):
        return self.scenario("fake").prompts()

    def return_scenario(self,user_data):
        return self.scenario(user_data.keys()[0])

class MockScenario(object):

    def __init__(self,string):
        self.string = string

    def setup(self):
        return "Fake Game Returned!"

    def prompts(self):
	return {"Fake Scenario Called!": ("acknowledge receipt")}

class MockPrompter(object):

    def __init__(self,display_object,user_input):
        self.display_method = display_object.display
	self.display_method("Mock Prompter Present!")
	self.user_input = user_input
	self.answers = []
	self.prompt_hash = {}

    def prompt_and_collect_input(self,prompts):
        for prompt in prompts:
            self.display_method(prompt)
	    answer = self.user_input.call()
            self.answers.append(answer)
	    self.prompt_hash[prompt] = answer

    def return_answer_hash(self):
        return self.prompt_hash

class UserInterfaceGameSetupTests(unittest.TestCase):

    def test_game_flow(self):
	user_input = MockUserInput(["give me a fake scenario","acknowledge receipt"])
	printer = FakePrinter()
	user_interface = UserInterface(user_input, printer, MockScenarioSelector, MockPrompter)
	game = user_interface.game_setup()
	displayed = printer.history_string()

	self.assertTrue("Fake Scenario Called!" in displayed) 
	self.assertTrue("Mock Selector Called!" in displayed) 
	self.assertTrue("Mock Prompter Present!" in displayed) 
	self.assertEqual("Fake Game Returned!",game)

        
        
