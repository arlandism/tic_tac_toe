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
        return self.minimax.next_move(self.board)

    def winner(self):
        return self.board.winner()

class Responder(object):
  
    def __init__(self,transmitter,generator=None):
        if generator is None:  generator = MoveGenerator()
        self.transmitter = transmitter
        self.generator = generator

    def respond(self):
        transmitter_data = self.transmitter.receive()
        comp_move = self.ai_move(transmitter_data)
        self.transmitter.send(comp_move)

    def ai_move(self, board_state):
        move_from_generator = self.generator.next_move(board_state)
        return move_from_generator
