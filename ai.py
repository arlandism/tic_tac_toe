from minimax import Minimax
from prompter import Prompter

class ImpossibleAI(object):

    def __init__(self,token,display_object=None,minimax=None):
        self.token = token
        if display_object is None:  display_object=Prompter()
        if minimax is None:  minimax=Minimax(self.token,20)
        self.minimax = minimax
        self.display_object = display_object

    def next_move(self,board):
        move = self.minimax.next_move(board)
        self.display_object.display(self.token.capitalize() + "'s turn" +
                                    self.token + " moves to " + str(move))
        return move
