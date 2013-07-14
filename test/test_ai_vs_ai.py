import unittest
from ai_vs_ai import AiVsAiScenario

class AiVsAiScenarioTests(unittest.TestCase):

    def test_that_ai_choice_shows_up(self):
      	prompt = "What difficulty would you like the first ai to be (easy,impossible): " 
        self.assertTrue(prompt in AiVsAiScenario.prompts({}))

    
