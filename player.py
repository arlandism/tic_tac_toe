from printer import Printer
from playerinput import InputValidator
from prompter import Prompter
from token_info import TokenInfo as ti

class HumanPlayer(object):

    def __init__(self,token,input_object=None,
                 display_object=None,prompter=None):
        if input_object is None:  input_object=Prompter()
        if display_object is None:  display_object=Prompter()
        if prompter is None:  prompter=Prompter()
        self.token = token
        self.opponent_token = ti.other_token(self.token)
        self.input_object = input_object
        self.display_object = display_object

    def next_move(self,board):
        moves = board.available_moves()
        info_string = (self.token.capitalize() + "'s turn" + "Please select a move: " +
                       "Available moves are " + str(moves))
        self.display_object.display(info_string)
        move = InputValidator.return_valid_response(self.input_object, board.available_moves())
        return move 

