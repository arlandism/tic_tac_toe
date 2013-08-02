from prompter import Prompter
from prompt_store import PromptStore

class UserInterface(object):

    def __init__(self,prompter=None,store=None):
        if prompter is None:  prompter = Prompter()
        if store is None:  store = PromptStore()
        self.prompter = prompter
        self.store = store

    def collected_data(self):
        self.prompter.prompt_and_collect_input(self.store.game_prompts)
        return self.prompter.return_answer_hash()
