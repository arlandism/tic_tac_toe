class MockSocket(object):
    
    def __init__(self):
        self.send_called = False
        self.receive_called = False
        self.send_args = []
        self.to_receive = []

    def send(self,string):
        self.send_args.append(string)
        self.send_called = True

    def recv(self,byte_length):
        self.receive_called = True
        return self.to_receive.pop() 

    def add_to_receive_stack(self,to_add):
        self.to_receive.append(to_add)
        
class MockBoard(object):
  
  def __init__(self,size):
      self.board_state = {}

  def state(self):
      return self.board_state

class MockTransmitter(object):

  def __init__(self,socket):
      self.times_sent_called = 0
      self.times_receive_called = 0
      self.send_args = []
      self.receive

  def send(self,to_send):
      self.times_sent_called += 1
      self.send_args.append(to_send)

  def receive(self):
      self.times_receive_called += 1

class MockServer(object):

  def __init__(self,host,port):
      self.accept_method_called = False
      self.send_called = False
      self.started = False
      self.close_called = False
      self.times_accept_called = 0

  def accept_connection_and_return_socket(self):
      self.times_accept_called += 1
      self.accept_method_called = True
      #returns client socket

  def send(self,to_send):
      self.send_called = True
      pass
    #sends to something

  def initialize_and_listen_for_connections(self):
      self.started = True
      #binds server to port
      #listens up to 1 queue request
      pass

  def close(self):
      self.close_called = True
      #closes
      pass
