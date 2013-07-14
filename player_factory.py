from player import HumanPlayer
from ai import ImpossibleAI
from humanoid import Humanoid
from minimax import Minimax

class PlayerFactory(object):

    @staticmethod
    def player(player_type,token):
        if player_type == "EasyAi":
            return ImpossibleAI(token,minimax=Minimax(token,1))
        players = {"Human":HumanPlayer,
                   "Humanoid":Humanoid,
                   "ImpossibleAI":ImpossibleAI}
        return players.get(player_type)(token)
