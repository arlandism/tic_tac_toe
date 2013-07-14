from win_generator import WinGenerator

class BaseBoard(object):

    def __init__(self,base=None):
        self.board_index = base
        if base is not None: 
            self.keys = range(1,self.board_index * self.board_index+1)
            self.WINNING_COMBINATIONS = WinGenerator(self.board_index).winners()
            self.board_state = dict()

    def __str__(self):
        board_template = []
        dashes = "-" * self.board_index * self.board_index
        left_side = "%("
        right_side = ")3s"
        for number in self.keys:
          if number % self.board_index == 0:
              board_template.append(left_side + str(number) + right_side + "\n" + dashes + "\n")
          else:
              board_template.append(left_side + str(number) + right_side)
        board_template = "".join(board_template)
        return board_template.rstrip("\n" + dashes) % self.generate_layout()

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

    def state(self):
        return self.board_state

    def generate_layout(self):
        keys_present = self.board_state.keys()
        keys_not_present = self.available_moves()
        layout = dict()
        for key in keys_present:
            layout[str(key)] = self.board_state[key]
        for key in keys_not_present:
             layout[str(key)] = ""
        return layout

