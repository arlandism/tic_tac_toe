import unittest

from game import Game
from user_interface import *
from test_utils import *

class MockScenarioSelector(object):

    def __init__(self,user_input,display_object):
        self.user_input = user_input
        self.display_object = display_object
        self.display_object.display("Mock Selector Called!")
        self.mapping = {"give me a fake scenario": MockScenario}
        self.scenario = self.mapping[user_input.call()]

    def scenario_prompts(self):
        return self.scenario("fake").prompts()

    def return_scenario(self,user_data):
        return self.scenario(user_data.keys()[0])

class MockStore(object):
    
    game_prompts = {"insert random prompt here":("any input will do","stuff")}

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

    def test_prompt_store_called(self):
        mock = MockUserInput(["any input will do"])
        fp = FakePrinter()
        ui = UserInterface(mock,fp,store=MockStore())

    def test_prompter_called(self):
        mock = MockUserInput(["stuff","Human"])
        prompter = MockPrompter
        fp = FakePrinter()
        ui = UserInterface(mock,fp,prompter=prompter,store=MockStore())
