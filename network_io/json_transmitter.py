import json

class HashTransformer(object):

      @staticmethod
      def try_dict_key_conversion(dictionary):
          new_dict = {}
          try:
            for key,val in dictionary.items():
                new_key = HashTransformer.try_int_conversion(key)
                new_dict[new_key] = val
            return  new_dict
          except:
              return dictionary

      @staticmethod
      def try_int_conversion(key):
          try:
              key = int(key)
          except:
              pass
          return key

      @staticmethod
      def is_terminal(thing):
          return False

class JsonTransmitter(object):

  END_MSG = "\r\n"

  def __init__(self,socket):
      self.socket = socket

  def send(self,message):
      message = json.dumps(message) 
      self.socket.send(message + self.END_MSG) 

  def receive(self):
      jsonified = self.socket.recv(4096)
      jsonified = jsonified.replace("\n","")
      dejsonified = json.loads(jsonified)
      return HashTransformer.try_dict_key_conversion(dejsonified) 
