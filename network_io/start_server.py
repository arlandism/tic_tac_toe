from server_socket import ServerSocket
from json_transmitter import JsonTransmitter
from responder import Responder, MoveGenerator
from response_handler import ResponseHandler

server = ServerSocket("localhost",5000)
server.initialize_and_listen_for_connections()

while True:
    connection_socket = server.accept_connection_and_return_socket()
    transmitter = JsonTransmitter(connection_socket)
    responder = Responder(transmitter,ResponseHandler(MoveGenerator()))
    responder.respond()
    connection_socket.close()
