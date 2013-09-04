import sys
import copy
sys.path.append("/Users/arlandislawrence/development/python/tic_tac_toe/")
from game.base_board import BaseBoard
from game.minimax import Minimax

class MoveGenerator(object):

    def __init__(self,board=None):
        if board is None:  board = BaseBoard(3)
        self.board = board

    def next_move(self,board_state,ai_depth=None):
        ai_depth = self.__error_check(ai_depth)
        self.board.set_state(board_state)
        comp_move = Minimax("o",ai_depth).next_move(self.board)
        self.board.make_move(comp_move,"o")
        return comp_move

    def winner_of(self,state):
        board = copy.copy(self.board)
        board.set_state(state)
        return board.winner()

    def winner(self):
        return self.board.winner()

    def __error_check(self,value):
        if value is None:
            ai_depth = 20
        else:
            ai_depth = self.__try_int_conversion_or_throw_exception(value)
        return ai_depth

    def __try_int_conversion_or_throw_exception(self,value):
        try: 
            ai_depth = int(value)
            return ai_depth
        except ValueError:
            raise MustBeInt

class MustBeInt(Exception):
    
    pass
