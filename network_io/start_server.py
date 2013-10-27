from optparse import OptionParser

from server_socket import ServerSocket
from json_transmitter import JsonTransmitter
from responder import Responder
from move_generator import MoveGenerator
from response_handler import ResponseHandler
from response_thread import ResponseThread

command_line_parser = OptionParser()
command_line_parser.add_option("-p", "--port", 
                               type="int", dest="port",
                               help="Port for the server to run on")
command_line_parser.set_defaults(port=5000)

(options, args) = command_line_parser.parse_args()

server = ServerSocket("localhost", options.port)
print "Server starting on port %d..."  % options.port
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



