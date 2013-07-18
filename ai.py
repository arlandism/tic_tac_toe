from minimax import Minimax
from prompter import Prompter

class ImpossibleAI(object):

    def __init__(self,token,prompter=None,minimax=None):
        self.token = token
        if prompter is None:  prompter=Prompter()
        if minimax is None:  minimax=Minimax(self.token,20)
        self.minimax = minimax
        self.prompter = prompter

    def next_move(self,board):
        move = self.minimax.next_move(board)
        self.prompter.display(self.token.capitalize() + "'s turn" +
                                    self.token + " moves to " + str(move))
        return move
