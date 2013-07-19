from base_board import BaseBoard
from board_generator import BoardStringGenerator
from prompter import Prompter
import sys

class Game(object):

    def __init__(self,player_one,player_two,board=None,prompter=None):
        if board is None:  board = BaseBoard(3)
      	if prompter is None:  prompter = Prompter()
        self.board = board
        self.player_one = player_one
        self.player_two = player_two
        self.prompter = prompter
        self.current_player = player_one
    
    def run(self):
        self.__introduction__()
        while not self.__over__():
            self.__round__()
        self.prompter.display(self.board)
        self.__print_winner__()

    def __print_winner__(self):
        if self.board.winner():
            self.prompter.display(self.board.winner() + " wins")
        else:
            self.prompter.display("It's a tie.")

    def __introduction__(self):
        #won't work with formatter
        #example_board = BoardStringGenerator(self.board.board_index).example_board()
        self.prompter.display("\nType quit and press Enter anytime to quit")

    def __round__(self):
        if not self.__over__():
            move = self.current_player.next_move(self.board)
            self.__move__(move,self.current_player)
        self.__alternate_player__()
        self.__print_board_if_game_not_over__()

    def __print_board_if_game_not_over__(self):
        if not self.__over__():
            self.prompter.display(self.board)

    def __over__(self):
        return self.board.over() 

    def __move__(self,space,player):
        self.board.make_move(space,player.token)

    def __alternate_player__(self):
        self.current_player = {self.player_one:self.player_two,
			                         self.player_two:self.player_one}[self.current_player]

