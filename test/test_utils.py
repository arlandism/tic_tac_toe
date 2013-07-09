from player import HumanPlayer
from board import Board
from string import ascii_letters


class MockUserInput(object):

    def __init__(self,vals):
        self.data = list(vals)
        self.times_called = 0

    def call(self):
        self.__increment_times_called__()
        return self.data.pop(0)

    def __increment_times_called__(self):
        self.times_called += 1

class MockPlayer(HumanPlayer):

    def __init__(self,token,fake_input):
        super(MockPlayer,self).__init__(token,fake_input)

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
	return str(self.history)

class MockScenario(object):

    def __init__(self):
	pass

    def setup(self):
	return "glitch in the matrix."

    @staticmethod
    def prompts():
	return {"any letter will do": ascii_letters}
