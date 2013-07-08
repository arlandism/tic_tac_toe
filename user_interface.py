from playerinput import InputValidator
from printer import Printer
from scenario_selector import ScenarioSelector
from ai_vs_ai import AiVsAiScenario
from humanoid_vs_ai import HumanoidVsAiScenario
from human_vs_human import HumanVsHumanScenario
from human_vs_ai import HumanVsAiScenario
from prompter import Prompter

class UserInterface(object):

    def __init__(self,user_input,display_object=Printer()):
        self.user_input = user_input
	self.display_object = display_object
        self.display_method = display_object.display
	self.scenario_mapping = {1:HumanVsAiScenario,2:HumanVsHumanScenario, 
			         3:AiVsAiScenario, 4:HumanoidVsAiScenario}

    def game_setup(self):
        scenario_prompt = ("Please choose a scenario: \n" +
                  "(1) Human vs AI\n" +
                  "(2) Human vs Human\n" +
                  "(3) AI vs AI\n" +
                  "(4) Humanoid vs AI")
	prompt_hash = dict()
	answer_choices = (1,2,3,4)
	prompt_hash[scenario_prompt] = answer_choices 
	prompter = Prompter(self.display_object,self.user_input)
	prompter.prompt_and_collect_input(prompt_hash)
	scenario_number = prompter.return_answer_hash()[scenario_prompt] 
	scenario_object = self.scenario_mapping[scenario_number]
	scenario_selector = ScenarioSelector(scenario_object)
	prompter.prompt_and_collect_input(scenario_selector.scenario_prompts())
	user_responses = prompter.return_answer_hash()
	scenario = scenario_selector.return_scenario(user_responses)
        return scenario.setup() 
