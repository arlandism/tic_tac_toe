from minimax import Minimax
from printer import Printer

class ImpossibleAI(object):

    def __init__(self,token,display_object=None,minimax=None):
        if display_object is None:  display_object=Printer()
      	self.token = token
        if minimax is None:  minimax=Minimax(self.token,20)
        self.minimax = minimax
        self.display_method = display_object.display

    def next_move(self,board):
        self.display_method(self.token.capitalize() + "'s turn")
        move = self.minimax.next_move(board)
        self.display_method(self.token + " moves to " + str(move))
        return move
