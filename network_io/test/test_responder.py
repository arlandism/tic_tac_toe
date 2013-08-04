import unittest
from responder import Responder
from web_io_test_utils import MockTransmitter
import json

class FakeMoveGenerator(object):
  def __init__(self, to_return):
    self.to_return = to_return
    self.argument_history = []

  def next_move(self, board_state):
    self.argument_history.append(board_state)
    return self.to_return

class ResponderTests(unittest.TestCase):

  easy_win_possible = {1:"o", 2:"o", 4:"x", 7:"x"}
  bottom_row_win_possible = {7:"o", 8:"o"}

#  def test_responds_with_something(self):
#    transmitter = MockTransmitter([{"something":""}])
#    responder = Responder(transmitter)
#    responder.respond()
#    self.assertEqual(1,transmitter.times_receive_called)
#
#  def test_returns_board_with_obvious_move(self):
#    transmitter = MockTransmitter([self.easy_win_possible])
#    responder = Responder(transmitter)
#    responder.respond()
#    self.assertEqual(transmitter.send_args[0], 3)
#
#  def test_returns_board_with_win_defeat(self):
#    transmitter = MockTransmitter([self.bottom_row_win_possible])
#    responder = Responder(transmitter)
#    responder.respond()
#    self.assertEqual(transmitter.send_args[0], 9)

#INTEGRATION
#############################################
#UNIT

  def test_response_with_best_move(self):
    transmitter = MockTransmitter([self.easy_win_possible])
    generator = FakeMoveGenerator(5)
    responder = Responder(transmitter,generator) 
    responder.respond()
    self.assertEqual(generator.to_return, 5)

  def test_calls_next_move_with_board_state(self):
    transmitter = MockTransmitter([self.easy_win_possible])
    generator = FakeMoveGenerator(5)
    responder = Responder(transmitter,generator) 
    responder.respond()
    self.assertGeneratorNextMoveCalledWith(generator,self.easy_win_possible)

  def assertGeneratorNextMoveCalledWith(self,generator,called_with):
      self.assertEqual(generator.argument_history[0], called_with)

#  def test_move_generator_delegates_to_ai(self):
#    board_state = {}
#    ai_move = 99
#    fake_ai = FakeMinimax(ai_move)
#    generator = MoveGenerator(fake_ai)
#    self.assertEqual(generator.next_move(board_state), ai_move)
#    self.assertEqual(generator.history[0], board_state)
#
#
#
