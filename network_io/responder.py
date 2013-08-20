import sys
sys.path.append("/Users/arlandislawrence/development/python/tic_tac_toe/")
from game.minimax import Minimax
from game.base_board import BaseBoard

class Responder(object):
  
    def __init__(self,transmitter,handler):
        self.transmitter = transmitter
        self.handler = handler

    def respond(self):
        transmitter_data = self.transmitter.receive()
        response = self.handler.response(transmitter_data)
        self.transmitter.send(response)

class ResponseHandler(object):

    def __init__(self,generator):
        self.generator = generator

    def response(self,data):
        board_state = data["board"]
        difficulty = self.__try_difficulty_extraction(data)
        response = { "move": self.generator.next_move(board_state,difficulty),
                     "winner": self.generator.winner()
                   }
        return response

    def __try_difficulty_extraction(self,data):
        try:
           difficulty = data["depth"]
        except KeyError:
           difficulty = None
        return difficulty

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
