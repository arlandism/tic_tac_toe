from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_ai import HumanVsAiScenario
from easy_vs_impossible_ai import EasyVsImpossibleAiScenario
from scenario_selector import ScenarioSelector
from test_utils import FakePrinter
import unittest

class ScenarioSelectorTests(unittest.TestCase):

    def setUp(self):
	self.user_data = {"Would you like to play as x or o: ": "x",
		          "Would you like to move first or second (1,2): ": 1,
		          "Would you to play against an easy or impossible ai: ": "easy"}

    def test_second_player_works(self):
	scenario_selector = ScenarioSelector(HumanVsAiScenario)
	self.user_data["Would you like to move first or second (1,2): "] = 2
	scenario = scenario_selector.return_scenario(self.user_data) 
	self.assertEqual("x",scenario.human_token)

    def test_first_player_works(self):
	scenario_selector = ScenarioSelector(HumanVsAiScenario)
	scenario = scenario_selector.return_scenario(self.user_data)
	self.assertEqual("x",scenario.human_token)

    def test_ai_vs_ai(self):
	scenario_selector = ScenarioSelector(AiVsAiScenario)
	self.user_data["What difficulty would you like the first ai to be (easy,impossible): "] = "easy"
	scenario = scenario_selector.return_scenario(self.user_data)
	#self.assertTrue(isinstance(scenario,EasyVsImpossibleAiScenario))
	
