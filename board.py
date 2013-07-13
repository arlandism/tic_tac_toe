from base_board import BaseBoard

class Board(BaseBoard):

    def __init__(self):
        super(Board,self).__init__(base=3)

    def __str__(self):
        board_template = ("\n%(1)3s|%(2)3s|%(3)3s\n------------" +
                          "\n%(4)3s|%(5)3s|%(6)3s\n------------" +
                          "\n%(7)3s|%(8)3s|%(9)3s")
        return board_template % self.generate_layout()

