import unittest

from prompt_parser import *
from prompt_store import PromptStore

class PromptParserTokenTests(unittest.TestCase):

    def setUp(self):
        self.token_one_prompt = PromptStore().first_token() 

    def test_first_token_x(self):
        user_data = {self.token_one_prompt:"x"}
        self.assertEqual("x",PromptParser(user_data).first_token())

    def test_first_token_o(self):
        user_data = {self.token_one_prompt: "o"}
        self.assertEqual("o",PromptParser(user_data).first_token())

    def test_second_token_x(self):
        user_data = {self.token_one_prompt:"o"}
        self.assertEqual("x",PromptParser(user_data).second_token())

    def test_second_token_o(self):
        user_data = {self.token_one_prompt:"x"}
        self.assertEqual("o",PromptParser(user_data).second_token())

class PromptParserPlayerTests(unittest.TestCase):

    def setUp(self):
        self.first_player_prompt = PromptStore().player_string()

    def test_first_player_humanoid(self):
        user_data = {self.first_player_prompt:"Humanoid"}
        self.assertEqual("Humanoid",PromptParser(user_data).first_player())

    def test_first_player_human(self):
        user_data = {self.first_player_prompt:"Human"}
        self.assertEqual("Human",PromptParser(user_data).first_player())

class PromptParserSecondPlayerTests(unittest.TestCase):
    
    def test_second_player_ai(self):
        user_data = {PromptStore().second_player():"ImpossibleAI"}
        self.assertEqual("ImpossibleAI",PromptParser(user_data).second_player())

    def test_second_player_human(self):
        user_data = {PromptStore().second_player():"Human"}
        self.assertEqual("Human",PromptParser(user_data).second_player())

class PromptParserBoardTests(unittest.TestCase):

    def setUp(self):
        self.board_prompt = PromptStore().board()

    def test_board_three(self):
        user_data = {self.board_prompt:3}
        self.assertEqual(3,PromptParser(user_data).board_size())

    def test_board_four(self):
        user_data = {self.board_prompt:4}
        self.assertEqual(4,PromptParser(user_data).board_size())
