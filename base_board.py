
class BaseBoard(object):

    board_state = dict()

    def make_move(self,space,token):
        self.board_state[space] = token

    def state(self):
        return self.board_state
