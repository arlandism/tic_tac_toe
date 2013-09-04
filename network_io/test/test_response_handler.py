import unittest
import mock

from response_handler import ResponseHandler
from move_generator import MoveGenerator

class ResponseHandlerTests(unittest.TestCase):

   def test_handler_returns_with_move_key(self):
       data = {"board":""}
       generator = mock.Mock()
       generator.next_move = mock.MagicMock(return_value="ai_move")
       response = ResponseHandler(generator).response(data)
       self.assertEqual("ai_move",response["move"])

   def test_handler_returns_winner_after_ai_move_key(self):
       data = {"board":""}
       generator = mock.Mock()
       generator.winner = mock.MagicMock(return_value="winner!")
       response = ResponseHandler(generator).response(data)
       self.assertEqual("winner!",response["winner"])

   def test_handler_returns_winner_on_board_key(self):
       data = {"board":"stuff"}
       generator = mock.Mock()
       generator.winner_of = mock.MagicMock(return_value="x")
       response = ResponseHandler(generator).response(data)
       generator.winner_of.assert_any_call("stuff")
       self.assertEqual("x",response["winner_on_board"])

class IntegrationWithMoveGeneratorTests(unittest.TestCase):

   def test_response_contains_updated_game_information(self):
       data = {"board": {1:"o", 2:"o",5:"x"},
               "depth": 20}
       response = ResponseHandler(MoveGenerator()).response(data)
       self.assertEqual(3,response["move"])
       self.assertEqual("o",response["winner"])
       self.assertEqual(None,response["winner_on_board"])

   def test_handler_defaults_difficulty_if_depth_not_set(self):
       data = {"board": {1:"x",2:"x",5:"o"}}
       handler = ResponseHandler(MoveGenerator())
       response = handler.response(data)
       self.assertEqual(3,response["move"])
