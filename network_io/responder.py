import sys
sys.path.append("/Users/arlandislawrence/development/python/tic_tac_toe/")
from game.minimax import Minimax
from game.base_board import BaseBoard

class MoveGenerator(object):

    def __init__(self,board=None):
        if board is None:  board = BaseBoard(3)
        self.board = board

    def next_move(self,board_state,ai_depth=None):
        if ai_depth is None:
            ai_depth = 20
        self.board.board_state = board_state
        comp_move = Minimax("o",ai_depth).next_move(self.board)
        self.board.board_state[comp_move] = "o"
        return comp_move

    def winner(self):
        return self.board.winner()

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
 
class Responder(object):
  
    def __init__(self,transmitter,handler):
        self.transmitter = transmitter
        self.handler = handler

    def respond(self):
        transmitter_data = self.transmitter.receive()
        response = self.handler.response(transmitter_data)
        self.transmitter.send(response)
