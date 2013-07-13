from board import Board
from printer import Printer

class Game(object):

    def __init__(self,player_one,player_two,board=None,display_object=None):
        if board is None:  board = Board()
        self.board = board 
        self.player_one = player_one
        self.player_two = player_two
      	if display_object is None:  display_object = Printer()
        self.display_method = display_object.display
        self.current_player = player_one
    
    def run(self):
        self.__introduction__()
        while not self.__over__():
            self.__round__()
        self.display_method(self.board)
        self.__print_winner__()

    def __print_winner__(self):
        if self.board.winner():
            self.display_method(self.board.winner() + " wins")
        else:
            self.display_method("It's a tie.")

    def __introduction__(self):
        self.display_method(("\n1|2|3\n-------" +
                             "\n4|5|6\n-------" +
                             "\n7|8|9\n"))

    def __round__(self):
        if not self.__over__():
            move = self.current_player.next_move(self.board)
            self.__move__(move,self.current_player)
        self.__alternate_player__()
        self.__print_board_if_game_not_over__()

    def __print_board_if_game_not_over__(self):
        if not self.__over__():
            self.display_method(self.board)

    def __over__(self):
        return self.board.over()

    def __move__(self,space,player):
        self.board.make_move(space,player.token)

    def __alternate_player__(self):
        self.current_player = {self.player_one:self.player_two,
			       self.player_two:self.player_one}[self.current_player]
