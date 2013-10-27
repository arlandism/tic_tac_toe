import json
import socket

from hash_transformer import HashTransformer

class JsonTransmitter(object):

  CLRF = "\r\n"

  def __init__(self,socket):
      self.socket = socket

  def send(self,message):
      message = json.dumps(message) 
      self.socket.send(message + self.CLRF) 
      self.socket.shutdown(socket.SHUT_WR)

  def receive(self):
      jsonified = self.socket.recv(4096)
      dejsonified = json.loads(jsonified)
      return HashTransformer.try_dict_key_conversion(dejsonified) 

