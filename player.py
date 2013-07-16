from playerinput import PlayerInput
from printer import Printer
from playerinput import InputValidator

class HumanPlayer(object):

    PLAYERS_DICT = {'x':'o','o':'x'}

    def __init__(self,token,input_object=PlayerInput(),
                 display_object=Printer()):
        self.token = token
        self.opponent_token = (self.PLAYERS_DICT[token])
        self.input_object = input_object
        self.display_method = display_object.display

    def next_move(self,board):
        self.display_method(self.token.capitalize() + "'s turn")
        self.display_method("Please select a move: ")
        self.display_method("Available moves are " + str(board.available_moves()))	
        move = InputValidator.return_valid_response(self.input_object, board.available_moves())
        return move 

