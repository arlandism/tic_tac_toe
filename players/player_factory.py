from player import HumanPlayer
from ai import ImpossibleAI
from humanoid import Humanoid
from game.minimax import Minimax
from io.prompter import Prompter

class PlayerFactory(object):

    @staticmethod
    def player(player_type,token,display_object=None):
        if display_object is None:  display_object=Prompter()
        players = {"Human":HumanPlayer(token,display_object),
                   "Humanoid":Humanoid(token,display_object),
                   "ImpossibleAI":ImpossibleAI(token,display_object),
                   "EasyAI":ImpossibleAI(token,display_object,Minimax(token,1))}
        return players.get(player_type)
