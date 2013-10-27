from server_socket import ServerSocket
from json_transmitter import JsonTransmitter
from responder import Responder
from move_generator import MoveGenerator
from response_handler import ResponseHandler
from response_thread import ResponseThread

server = ServerSocket("localhost",5000)
server.initialize_and_listen_for_connections()

while True:
    try:
      connection_socket = server.accept_connection_and_return_socket()
      transmitter = JsonTransmitter(connection_socket)
      move_generator = MoveGenerator()
      handler = ResponseHandler(move_generator)
      responder = Responder(transmitter, handler)
      ResponseThread(responder).start()
    except KeyboardInterrupt:
      print "\nShutting down server..."
      break

