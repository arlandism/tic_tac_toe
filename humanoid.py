from minimax import Minimax
from prompter import Prompter
from playerinput import InputValidator

class Humanoid(object):

    def __init__(self, token, prompter=None, minimax=None):
        self.token = token
        if prompter is None:  prompter=Prompter()
        if minimax is None:  minimax=Minimax(self.token,6)
        self.prompter = prompter
        self.minimax = minimax
        self.times_next_move_called = 0

    def next_move(self,board):
        self.prompter.display(self.token.capitalize() + " turn")
        self.times_next_move_called += 1
        if self.times_next_move_called < 3:
	          move = self.__human_intervention__(board)
        else:
	          move =  self.minimax.next_move(board)
        self.prompter.display(self.token.capitalize() + " moves to " + str(move))
        return move

    def __human_intervention__(self,board):
        move_string = ("Please select a move: \n" + "Available moves are " +
                      str(board.available_moves()))
        self.prompter.display(move_string)
        move = InputValidator.return_valid_response(self.prompter,board.available_moves())
        return move	
