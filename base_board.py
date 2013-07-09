
class BaseBoard(object):

    def __init__(self,base=None):
        self.board_index = base

    board_state = dict()

    def make_move(self,space,token):
        self.board_state[space] = token

    def rows(self):
        keys = range(1,self.board_index * self.board_index+1)
        row_list = []
        index_one = 0
        for i in range(self.board_index):
            row_list.append(keys[index_one:index_one+self.board_index])
            index_one += self.board_index
        return row_list


    def state(self):
        return self.board_state
