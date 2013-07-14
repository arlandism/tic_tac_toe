from printer import Printer
from scenario_selector import ScenarioSelector
from prompter import Prompter
from prompt_store import PromptStore
from game_builder import GameBuilder

class UserInterface(object):

    def __init__(self,user_input=None,display_object=None,
                 selector=None,prompter=None,store=None):
        if display_object is None:  display_object = Printer()
        if user_input is None:  user_input = PlayerInput()
        if selector is None:  selector = ScenarioSelector
      	if prompter is None:  prompter = Prompter
        if store is None:  store = PromptStore()
        self.user_input = user_input
      	self.display_object = display_object
        self.prompter = prompter(display_object,user_input)
        self.store = store

    def game_setup(self):
        self.prompter.prompt_and_collect_input(self.store.game_prompts)
        user_data = self.prompter.return_answer_hash() 
        return GameBuilder.game(user_data)
