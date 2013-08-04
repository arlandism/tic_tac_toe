class MockUserInput(object):

    def __init__(self,vals):
        self.data = list(vals)
        self.times_called = 0

    def call(self):
        self.__increment_times_called__()
        try:
            return self.data.pop(0)
        except IndexError:
            print "Sorry, nothing left"

    def __increment_times_called__(self):
        self.times_called += 1

class SimpleMockPrompter(object):

    def __init__(self,vals=None):
        if vals is None:  vals = []
        self.vals = vals
        self.history = []
        self.times_called = 0

    def call(self):
        self.times_called += 1
        return self.vals.pop(0)

    def display(self,x):
        self.history.append(x)
        print x

    def history_string(self):
        return "".join(self.history)


class FakePrinter(object):

    def __init__(self):
        self.history = []

    def display(self,item):
        self.history.append(item.__str__())
        print item

    def last_print(self):
        try:
            return self.history.pop()
        except IndexError:
            print "history must be populated."
            return []

    def history_string(self):
	      history_string = "".join(self.history)
	      return history_string


class FakeMinimax(object):

    def next_move(self,board):
        return "next move"

class MockPrompter(object):

    def __init__(self,display_object,user_input):
        self.display_method = display_object.display
        self.display_method("Mock Prompter Present!")
        self.user_input = user_input
        self.answers = []
        self.prompt_hash = {}

    def prompt_and_collect_input(self,prompts):
        for prompt in prompts:
            self.display_method(prompt)
            answer = self.user_input.call()
            self.answers.append(answer)
            self.prompt_hash[prompt] = answer

    def return_answer_hash(self):
        return self.prompt_hash

class MockStore(object):
    
    game_prompts = {"insert random prompt here":""}

class MockParser(object):

    def __init__(self,user_data):
        self.user_data = user_data

    def first_player(self):
        return self.user_data["Player One"]

    def first_token(self):
        return "x"

    def second_player(self):
        return self.user_data["Player Two"]

    def second_token(self):
        return "o"

    def board_size(self):
        return self.user_data["board"] 
        return self.gameboard.size
