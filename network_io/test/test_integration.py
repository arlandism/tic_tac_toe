import unittest
import socket
import json
import sys
import random
import mock

sys.path.append("../")
from game.base_board import BaseBoard
from server_socket import ServerSocket
from json_transmitter import JsonTransmitter
from responder import Responder, MoveGenerator

class ResponderIntegrationTests(unittest.TestCase):

      easy_win_possible = {1:"o", 2:"o", 4:"x", 7:"x"}

      def test_returns_board_with_obvious_move(self):
          transmitter = mock.Mock()
          transmitter.receive = mock.MagicMock(return_value=self.easy_win_possible)
          generator = MoveGenerator()
          responder = Responder(transmitter,generator)
          responder.respond()
          transmitter.send.assert_any_call(3)
        
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
          PORT = random.randint(2000,60000)
          server = ServerSocket("localhost",PORT)
          server.initialize_and_listen_for_connections()
          sock = socket.socket() 
          sock.connect(("localhost",PORT))
          connection_socket = server.accept_connection_and_return_socket()
          transmitter = JsonTransmitter(connection_socket)
          responder = Responder(transmitter)

          to_send = json.dumps({1:"o",3:"o"})
          sock.send(to_send)
          responder.respond()
          comp_move = sock.recv(1024)
          winner_status = sock.recv(1024)

          END_MSG_TERM  = "\r\n"
          self.assertEqual(json.dumps(2) + END_MSG_TERM,comp_move)
          self.assertEqual(json.dumps("o") + END_MSG_TERM, winner_status)
          
          sock.close()
          connection_socket.close()