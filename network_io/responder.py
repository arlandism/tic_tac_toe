import sys
sys.path.append("../")
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
