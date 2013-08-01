import json

class HashTransformer(object):

      @staticmethod
      def dict_keys_to_ints(dictionary):
          new_dict = {}
          try:
            for key,val in dictionary.items():
                try:
                    new_key = int(key)
                except:
                    new_key = key
                new_dict[new_key] = val
            return  new_dict
          except:
              return dictionary

class JsonTransmitter(object):

  def __init__(self,socket):
      self.socket = socket

  def send(self,message):
      message = json.dumps(message) 
      self.socket.send(message)

  def receive(self):
      jsonified = self.socket.recv(4096)
      jsonified = jsonified.replace("\n","")
      dejsonified = json.loads(jsonified)
      return HashTransformer.dict_keys_to_ints(dejsonified) 
