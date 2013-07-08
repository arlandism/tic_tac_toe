
from game import Game
from easy_ai import EasyAI
from ai import ImpossibleAI

class EasyVsImpossibleAiScenario(object):

    def setup(self):
        return Game(EasyAI("x"),ImpossibleAI("o")) 
