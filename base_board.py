
class BaseBoard(object):

    def __init__(self,base=None):
        self.board_index = base
        if base is not None: self.keys = range(1,self.board_index * self.board_index+1)

    board_state = dict()

    def make_move(self,space,token):
        self.board_state[space] = token

    def rows(self):
        row_list = []
        index_one = 0
        for i in range(self.board_index):
            row_list.append(self.keys[index_one:index_one+self.board_index])
            index_one += self.board_index
        return row_list

    def columns(self):
        column_list = []
        for i in range(self.board_index):
            column = []
            for j in range(self.board_index):
                column.append(self.keys[i])
                i += self.board_index
            column_list.append(column)
        return column_list

    def diagonals(self):
        diagonal_list = []
        diagonal = []
        second_diagonal = []
        board_key = 1
        alt_board_key = board_key + self.board_index - 1
        for i in range(self.board_index):
            diagonal.append(board_key)
            board_key += self.board_index + 1
            second_diagonal.append(alt_board_key)
            alt_board_key += self.board_index - 1
        diagonal_list.append(diagonal)
        diagonal_list.append(second_diagonal)
        return diagonal_list


    def state(self):
        return self.board_state
