from prompter import Prompter
from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_human import HumanVsHumanScenario
from human_vs_ai import HumanVsAiScenario
from playerinput import PlayerInput
from printer import Printer

class ScenarioSelector(object):

    def return_scenario(self,user_data):
        return self.scenario(user_data)

    def prompts(self):
        return "Board size please... "
