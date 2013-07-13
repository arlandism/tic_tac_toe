from minimax import Minimax
from game import Game
from ai import ImpossibleAI

class EasyVsImpossibleAiScenario(object):

    def setup(self):
        return Game(ImpossibleAI("x",minimax=Minimax("x",1)),ImpossibleAI("o"))
