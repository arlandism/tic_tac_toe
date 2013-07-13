from minimax import Minimax
from printer import Printer

class ImpossibleAI(object):

    def __init__(self,token,display_object=Printer()):
      	self.token = token
        self.display_method = display_object.display

    def next_move(self,board,minimax=None):
        if not minimax:
            minimax = Minimax(self.token,6)
        self.display_method(self.token.capitalize() + "'s turn")
        move = minimax.next_move(board)
        self.display_method(self.token + " moves to " + str(move))
        return move
