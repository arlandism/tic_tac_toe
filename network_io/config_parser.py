
class ConfigParser(object):

    def __init__(self,file_to_parse):
        self.to_parse = file_to_parse
         
    def token(self):
        return self.__find_it("token")

    def player_one(self):
        return self.__find_it("player_one")

    def player_two(self):
        return self.__find_it("player_two")

    def difficulty(self):
        return int(self.__find_it("depthlimit"))
        
    def __find_it(self,to_find):
        PREFIX_LEN = len(to_find) + len(": ")
        start = self.to_parse.find(to_find + ": ") + PREFIX_LEN
        END_OF_VAL = self.to_parse[start: ].find("\n")
        found = self.to_parse[start:start + END_OF_VAL] 
        return found
