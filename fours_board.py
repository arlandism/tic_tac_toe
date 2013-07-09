

class FourByFourBoard(object):

    board_state = {}

    def over(self):
        if self.board_state:
            return True
        return False
