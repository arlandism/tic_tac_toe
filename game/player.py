from io.playerinput import InputValidator
from io.prompter import Prompter
from token_info import TokenInfo as ti

class HumanPlayer(object):

    def __init__(self,token,prompter=None):
        if prompter is None:  prompter=Prompter()
        self.token = token
        self.prompter = prompter

    def next_move(self,board):
        moves = board.available_moves()
        info_string = (self.token.capitalize() + " turn" + "\nPlease select a move: " +
                       "\nAvailable moves are " + str(moves))
        self.prompter.display(info_string)
        move = InputValidator.return_valid_response(self.prompter, board.available_moves())
        return move 

