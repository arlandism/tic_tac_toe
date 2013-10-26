class ResponseHandler(object):

    def __init__(self,generator):
        self.generator = generator

    def response(self,data):
        board_state = data["board"]
        difficulty = self.__try_difficulty_extraction(data)
        response = { 
                     "ai_move": self.generator.next_move(board_state,difficulty),
                     "winner_after_ai_move": self.generator.winner(),
                     "winner_on_board": self.generator.winner_of(board_state)
                   }
        return response

    def __try_difficulty_extraction(self,data):
        try:
           difficulty = data["depth"]
        except KeyError:
           difficulty = None
        return difficulty

