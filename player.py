from printer import Printer
from playerinput import InputValidator
from prompter import Prompter

class HumanPlayer(object):

    PLAYERS_DICT = {'x':'o','o':'x'}

    def __init__(self,token,input_object=None,
                 display_object=None):
        if input_object is None:  input_object=Prompter()
        if display_object is None:  display_object=Prompter()
        self.token = token
        self.opponent_token = (self.PLAYERS_DICT[token])
        self.input_object = input_object
        self.display_object = display_object
        self.display_method = display_object.display

    def next_move(self,board):
        self.display_method(self.token.capitalize() + "'s turn")
        self.display_method("Please select a move: ")
        self.display_method("Available moves are " + str(board.available_moves()))	
        move = InputValidator.return_valid_response(self.input_object, board.available_moves())
        return move 

