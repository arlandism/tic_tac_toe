import sys
sys.path.append("/Users/arlandislawrence/development/python/tic_tac_toe/")
from game.minimax import Minimax
from game.base_board import BaseBoard

class MoveGenerator(object):

    def __init__(self,board=None,minimax=None):
        if board is None:  board = BaseBoard(3)
        if minimax is None:  minimax = Minimax("o",20)
        self.board = board
        self.minimax = minimax

    def next_move(self,board_state):
        self.board.board_state = board_state
        comp_move = self.minimax.next_move(self.board)
        self.board.board_state[comp_move] = self.minimax.token
        return comp_move

    def winner(self):
        return self.board.winner()

    def response(self,data):
        next_move = self.next_move(data["board"])
        winner = self.winner()
        return {"move": next_move,
                "winner": winner}

class Responder(object):
  
    def __init__(self,transmitter,generator):
        self.transmitter = transmitter
        self.generator = generator

    def respond(self):
        transmitter_data = self.transmitter.receive()
        response = self.generator.response(transmitter_data)
        self.transmitter.send(response)
