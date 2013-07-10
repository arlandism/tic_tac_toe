from win_generator import WinGenerator

class BaseBoard(object):

    def __init__(self,base=None):
        self.board_index = base
        if base is not None: self.keys = range(1,self.board_index * self.board_index+1)

    board_state = dict()

    def make_move(self,space,token):
        self.board_state[space] = token

    def winners(self):
        return WinGenerator(self.board_index).winners()

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

    def state(self):
        return self.board_state

