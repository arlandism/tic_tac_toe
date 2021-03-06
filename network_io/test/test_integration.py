import unittest
import socket
import json
import sys
import random
import mock

sys.path.append("../")
from game.base_board import BaseBoard
from game.minimax import Minimax
from server_socket import ServerSocket
from json_transmitter import JsonTransmitter
from responder import Responder
from move_generator import MoveGenerator
from response_handler import ResponseHandler

class ResponderIntegrationTests(unittest.TestCase):

      easy_win_possible = {"board":{1:"o", 2:"o", 4:"x", 7:"x"}}

      def test_returns_board_with_obvious_move(self):
          transmitter = mock.Mock()
          transmitter.receive = mock.MagicMock(return_value=self.easy_win_possible)
          generator = MoveGenerator()
          handler = ResponseHandler(generator)          
          responder = Responder(transmitter,handler)
          responder.respond()
          transmitter.send.called_with( {"winner_after_ai_move":"o","ai_move":3} )

class MoveGeneratorBaseBoardIntegrationTests(unittest.TestCase):

      def test_board_gets_updated_and_shows_win(self):
          easy_win = {1:"o", 2:"o"}
          WIN_MOVE = 3
          board = BaseBoard(3)
          generator = MoveGenerator(board)
          self.assertEqual(WIN_MOVE, generator.next_move(easy_win))
          self.assertEqual( {1:"o",2:"o",3:"o"}, board.state())

class HighLevelResponderTests(unittest.TestCase):

      def test_it_hooks_into_socket_sends_and_receives(self):
          transmitter = JsonTransmitter(self.connection_socket)
          handler = ResponseHandler(MoveGenerator())
          responder = Responder(transmitter,handler)

          game_info = json.dumps({ "board": {1:"o",3:"o"},
                                   "depth": 20 })
          self.sock.send(game_info)
          responder.respond()

          data_received = self.sock.recv(1024)
          updated_game = json.loads(data_received)
           
          WIN_MOVE = 2
          self.assertEqual(WIN_MOVE, updated_game["ai_move"])
          self.assertEqual("o" ,updated_game["winner_after_ai_move"])
          self.assertEqual(None, updated_game["winner_on_board"])
          
      def setUp(self):
          PORT = random.randint(2000,60000)
          self.server = ServerSocket("localhost",PORT)
          self.server.initialize_and_listen_for_connections()
          self.sock = socket.socket()
          self.sock.connect(("localhost",PORT))
          self.connection_socket = self.server.accept_connection_and_return_socket()

      def tearDown(self):
          self.sock.close()
          self.connection_socket.close()
