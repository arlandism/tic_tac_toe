
class MockSocket(object):

  def __init__(self):
      self.sent_stuff = []

  def send_data(self,x):
      self.sent_stuff.append(x)
      return 'some stuff'

  def receive_data(self):
      return 'got some stuff'
