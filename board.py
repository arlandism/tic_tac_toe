from base_board import BaseBoard

class Board(BaseBoard):

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

