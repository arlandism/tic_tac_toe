import unittest
import mock

from response_handler import ResponseHandler
from move_generator import MoveGenerator

class ResponseHandlerTests(unittest.TestCase):

   def test_handler_returns_human_vs_human_winner(self):
       data = {"board":"stuff"}
       generator = mock.Mock()
       generator.winner_of = mock.MagicMock(return_value="x")
       response = ResponseHandler(generator).response(data)
       generator.winner_of.assert_any_call("stuff")
       self.assertEqual("x",response["winner_on_board"])

class IntegrationWithMoveGeneratorTests(unittest.TestCase):

   def test_response_delegates_to_move_generator(self):
       data = {"board": {1:"x",2:"x",5:"o"},
               "depth": 20}
       handler = ResponseHandler(MoveGenerator())
       response = handler.response(data)
       self.assertEqual(3,response["move"])
       self.assertEqual(None,response["winner"])

   def test_handler_defaults_difficulty_if_depth_not_set(self):
       data = {"board": {1:"x",2:"x",5:"o"}}
       handler = ResponseHandler(MoveGenerator())
       response = handler.response(data)
       self.assertEqual(3,response["move"])

    
