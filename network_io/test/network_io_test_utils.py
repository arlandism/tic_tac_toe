class MockSocket(object):
    
    def __init__(self):
        self.send_called = False
        self.receive_called = False
        self.shutdown_called = False
        self.send_args = []
        self.to_receive = []
        self.shutdown_args = []

    def send(self,string):
        self.send_args.append(string)
        self.send_called = True

    def recv(self,byte_length):
        self.receive_called = True
        return self.to_receive.pop() 

    def add_to_receive_stack(self,to_add):
        self.to_receive.append(to_add)

    def shutdown(self, param):
        self.shutdown_args.append(param)        
        self.shutdown_called = True

    def shutdown_called_with(self, arg):
        return arg in self.shutdown_args and self.shutdown_called
        

