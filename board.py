from base_board import BaseBoard

class Board(BaseBoard):

    WINNING_COMBOS = [[1,2,3],[4,5,6],[7,8,9],
                      [1,4,7],[2,5,8],[3,6,9],
                      [1,5,9], [3,5,7]]

    def __init__(self):
        self.board_state = dict()
        self.board_index = 3
        self.keys = range(1,10)

    def __str__(self):
        board_template = ("\n%(1)3s|%(2)3s|%(3)3s\n------------" +
                          "\n%(4)3s|%(5)3s|%(6)3s\n------------" +
                          "\n%(7)3s|%(8)3s|%(9)3s")
        return board_template % self.generate_layout()

    def generate_layout(self):
        keys_present = self.board_state.keys()
        keys_not_present = self.available_moves()
        layout = dict()
        for key in keys_present:
            layout[str(key)] = self.board_state[key]
        for key in keys_not_present:
             layout[str(key)] = ""
        return layout

    def over(self):
        return bool(self.winner()) or self.is_full()

    def winner(self):
        for combo in self.WINNING_COMBOS:
            if self.__pieces_match__(combo):
                    return self.board_state[combo[0]]

    def generate_winners(self):
        pass

    def is_full(self):
        occupied_spaces = self.board_state.keys()
        return occupied_spaces == range(1,10)

    def available_moves(self):
        spaces_taken = self.board_state.keys()
        move_list = range(1,10)
        available_moves = [move for move in move_list if move not in spaces_taken]
        return available_moves


    def __pieces_match__(self,combo):
        occupied_spaces = self.board_state.keys()
        if combo[0] in occupied_spaces and combo[1] in occupied_spaces and combo[2] in occupied_spaces:
            first_piece = self.board_state[combo[0]]
            second_piece = self.board_state[combo[1]]
            third_piece = self.board_state[combo[2]]
            return first_piece == second_piece == third_piece
        return False

    def erase_move(self,move):
        del self.board_state[move]
