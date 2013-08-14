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
        

