from minimax import Minimax
from printer import Printer

class EasyAI(object):

    def __init__(self,token,display_object=Printer()):
	self.token = token
	self.display_method = display_object.display

    def next_move(self,board,minimax=None):
        if not minimax:
            minimax = Minimax(self.token,1)
	move = minimax.next_move(board)
	self.display_method(self.token.capitalize() + "'s turn")
	self.display_method(self.token.capitalize() + " moves to " + str(move))
	return move

