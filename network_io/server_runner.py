
class ServerRunner(object):

    def __init__(self,server):
        self.server = server
        self.server_started = False

    def start_server(self):
        self.server.initialize_and_listen_for_connections()
        self.server_started = True

    def accept_connections(self):
        if self.server_started:
            self.server.accept_connection_and_return_socket()
        else:
            raise ServerOffException
        

class ServerOffException(Exception):
    pass
