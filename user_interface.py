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
    	self.scenario_mapping = {1:HumanVsAiScenario,2:HumanVsHumanScenario, 
			                    3:AiVsAiScenario, 4:HumanoidVsAiScenario}
    	self.scenario_prompt = ("Please choose a scenario: \n" +
                                "(1) Human vs AI\n" +
                                "(2) Human vs Human\n" +
                                "(3) AI vs AI\n" +
                                "(4) Humanoid vs AI")
    	self.scenario_choices = (1,2,3,4)


    def game_setup(self):
	    prompter = Prompter(self.display_object,self.user_input)
	    prompter.prompt_and_collect_input({self.scenario_prompt: self.scenario_choices}) 
	    chosen_scenario_number = prompter.return_answer_hash()[self.scenario_prompt] 
	    chosen_scenario = self.scenario_mapping[chosen_scenario_number]
	    prompter.prompt_and_collect_input(chosen_scenario.prompts())
	    user_responses = prompter.return_answer_hash()
	    return chosen_scenario(user_responses).setup() 
