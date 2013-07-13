from printer import Printer
from scenario_selector import ScenarioSelector
from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_human import HumanVsHumanScenario
from human_vs_ai import HumanVsAiScenario
from prompter import Prompter

class UserInterface(object):

    def __init__(self,user_input=None,display_object=None,
                 selector=None,prompter=None):
        if display_object is None:  display_object = Printer()
        if user_input is None:  user_input = PlayerInput()
        if selector is None:  selector = ScenarioSelector
      	if prompter is None:  prompter = Prompter
        self.user_input = user_input
      	self.display_object = display_object
        self.selector = selector(user_input,display_object)
        self.prompter = prompter(display_object,user_input)

    def game_setup(self):
        self.prompter.prompt_and_collect_input(self.selector.scenario_prompts())
        user_responses = self.prompter.return_answer_hash()
        scenario = self.selector.return_scenario(user_responses)
        return scenario.setup()
