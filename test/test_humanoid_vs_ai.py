import unittest
from humanoid_vs_ai import HumanoidVsAiScenario
from game import Game
from humanoid import Humanoid
from easy_ai import EasyAI
	
class HumanoidVsAiScenarioSetupTests(unittest.TestCase):

    def setUp(self):
       	self.user_data = {"Would you like to play as x or o: ": "x",
			  "Would you like to move first or second (1,2): ": 1, 
			  "Would you like to play against an easy or impossible ai: ": "easy"}
    
    def test_that_it_returns_game_object(self):
        scenario = HumanoidVsAiScenario(self.user_data)
        game = scenario.setup()
        self.assertTrue(isinstance(game,Game))
	
    def test_that_it_set_correct_player_order(self):
        scenario = HumanoidVsAiScenario(self.user_data)
        game = scenario.setup()
        player_one = game.player_one
        self.assertTrue(isinstance(player_one,Humanoid))
	
    def test_that_it_works_with_easy_ai(self):
        scenario = HumanoidVsAiScenario(self.user_data)
        game = scenario.setup()
        player_two = game.player_two
        # Test for dummy ai
