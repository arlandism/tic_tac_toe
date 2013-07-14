from printer import Printer
from playerinput import PlayerInput,InputValidator

class Prompter(object):

    def __init__(self,display_object=None,input_object=None):
        if display_object is None:  display_object = Printer()
        if input_object is None:  input_object = PlayerInput()
        self.display_method = display_object.display
        self.input_object = input_object
        self.answers = []
        self.prompt_hash = {}

    def prompt_and_collect_input(self,ordered_prompt_hash):
        for prompt in ordered_prompt_hash.keys():
            self.display_method(prompt)
            answer = InputValidator.return_valid_response(self.input_object,ordered_prompt_hash[prompt])
            self.answers.append(answer)
            self.prompt_hash[prompt] = answer

    def return_answers(self):
        return self.answers

    def return_answer_hash(self):
        return self.prompt_hash
