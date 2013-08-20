from win_generator import WinGenerator
from board_generator import BoardStringGenerator

class BaseBoard(object):

    def __init__(self,base=None):
        self.board_index = base
        if base is not None: 
            self.keys = range(1,self.board_index * self.board_index+1)
            self.WINNING_COMBINATIONS = WinGenerator(self.board_index).winners()
            self.board_state = dict()

    def __str__(self):
        generator = BoardStringGenerator(self.board_index,self.state())
        return generator.generate_template() % generator.generate_layout()

    def make_move(self,space,token):
        self.board_state[space] = token

    def winners(self):
        return self.WINNING_COMBINATIONS

    def winner(self):
        for combo in self.winners():
            if self.moves_have_been_made(combo):
                if self.pieces_match(combo):
                    return self.winning_token(combo) 

    def pieces_match(self,combo):
        tokens = [self.board_state[space] for space in combo] 
       	return tokens[1:] == tokens[:-1]

    def moves_have_been_made(self,combo):
        return set(combo).issubset(set(self.state().keys()))

    def winning_token(self,combo):
        return self.board_state[combo[0]]
    
    def is_full(self):
        return self.state().keys() == self.keys

    def over(self):
        return bool(self.winner()) or self.is_full() 

    def available_moves(self):
        moves_taken = self.state().keys()
        return [move for move in self.keys if move not in moves_taken] 

    def erase_move(self,move):
        del self.board_state[move]

    def set_state(self,new_state):
        self.board_state = new_state

    def state(self):
        current_state = {}
        for key in self.board_state:
            if key in self.keys:
              current_state[key] = self.board_state[key]
        return current_state
