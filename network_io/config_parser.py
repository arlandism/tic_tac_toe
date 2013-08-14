
class ConfigParser(object):

    def __init__(self,file_to_parse):
        self.to_parse = file_to_parse
         
    def first_token(self):
        found = self.__find_it("first_token")
        return self.__found_or_default(found,"x")

    def player_one(self):
        found = self.__find_it("player_one") 
        return self.__found_or_default(found,"Human")

    def player_two(self):
        found =  self.__find_it("player_two")
        return self.__found_or_default(found,"ImpossibleAI")

    def difficulty(self):
        found = self.__find_it("depthlimit")
        return int(self.__found_or_default(found,20))

    def board_size(self):
        found = self.__find_it("board_size")
        return int(self.__found_or_default(found,3))

    def __found_or_default(self,found,default):
        if found:
            return found
        else:
            return default
        
    def __find_it(self,to_find):
        PREFIX_LEN = len(to_find) + len(": ")
        start = self.to_parse.find(to_find + ": ") + PREFIX_LEN
        END_OF_VAL = self.to_parse[start: ].find("\n")
        found = self.to_parse[start:start + END_OF_VAL] 
        return found
