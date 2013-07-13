import unittest

from prompter import Prompter
from ai_vs_ai import AiVsAiScenario
from human_vs_ai import HumanVsAiScenario
from scenario_selector import ScenarioSelector
from humanoid_vs_ai import HumanoidVsAiScenario
from easy_vs_impossible_ai import EasyVsImpossibleAiScenario

from test_utils import * 

class ScenarioSelectorTests(unittest.TestCase):

    def setUp(self):
	self.user_data = {"Would you like to play as x or o: ": "x",
		          "Would you like to move first or second (1,2): ": 1,
		          "Would you to play against an easy or impossible ai: ": "easy"}

    def test_second_player_works(self):
        ui = MockUserInput([1])
	scenario_selector = ScenarioSelector(ui)
	self.user_data["Would you like to move first or second (1,2): "] = 2
	scenario = scenario_selector.return_scenario(self.user_data) 
	self.assertEqual("x",scenario.human_token)

    def test_first_player_works(self):
        ui = MockUserInput([1])
	scenario_selector = ScenarioSelector(ui)
	scenario = scenario_selector.return_scenario(self.user_data)
	self.assertEqual("x",scenario.human_token)

    def test_scenario_setup_prompts(self):
        ui = MockUserInput([1])
        fp = FakePrinter()
	ss = ScenarioSelector(ui,fp)
	scenario_prompts = ("Please choose a scenario: \n" +
                            "(1) Human vs AI\n" +
                            "(2) Human vs Human\n" +
                            "(3) AI vs AI\n" +
                            "(4) Humanoid vs AI")
	self.assertTrue(scenario_prompts in fp.history_string())

