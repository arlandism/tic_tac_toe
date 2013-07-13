from prompter import Prompter
from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_human import HumanVsHumanScenario
from human_vs_ai import HumanVsAiScenario
from playerinput import PlayerInput
from printer import Printer

class ScenarioSelector(object):

    def __init__(self,input_object=None,display_object=None):
	if input_object is None:  input_object = PlayerInput()
	if display_object is None:  display_object = Printer()
	self.prompter = Prompter(display_object,input_object)
        self.prompt = ("Please choose a scenario: \n" +
                       "(1) Human vs AI\n" +
                       "(2) Human vs Human\n" +
                       "(3) AI vs AI\n" +
                       "(4) Humanoid vs AI")
	self.prompter.prompt_and_collect_input({self.prompt:(1,2,3,4)})
	self.mapping = {1:HumanVsAiScenario,2:HumanVsHumanScenario,
                        3:AiVsAiScenario,4:HumanoidVsAiScenario}
	self.scenario = self.mapping[self.prompter.return_answer_hash()[self.prompt]]

    def return_scenario(self,user_data):
        return self.scenario(user_data)

    def scenario_prompts(self):
	return self.scenario.prompts()
