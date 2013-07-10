from base_board import BaseBoard

class FourByFourBoard(BaseBoard):

    def __init__(self):
        super(FourByFourBoard,self).__init__(base=4)

    def __str__(self):  
        board_template = ("\n%(1)3s|%(2)3s|%(3)3s|%(4)3s\n---------------" +
                          "\n%(5)3s|%(6)3s|%(7)3s|%(8)3s\n---------------" +
                          "\n%(9)3s|%(10)3s|%(11)3s|%(12)3s\n---------------" +
			  "\n%(13)3s|%(14)3s|%(15)3s|%(16)3s\n")
        return board_template % self.generate_layout() 
