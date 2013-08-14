import unittest
from config_parser import ConfigParser

class ConfigParserTests(unittest.TestCase):

    fake_config_file = ("token: test_token\n" +
                        "player_one: test_player_one\n" +
                        "player_two: test_player_two\n" +
                        "difficulty: juggernaut\n")

    def setUp(self):
        self.parser= ConfigParser(self.fake_config_file)

    def test_reads_from_input_for_token(self):
        token = self.parser.token()
        self.assertEqual("test_token",token)
        
    def test_reads_from_input_for_player_one(self):
        player = self.parser.player_one()
        self.assertEqual("test_player_one",player)
        
    def test_reads_from_input_for_player_two(self):
        player = self.parser.player_two()
        self.assertEqual("test_player_two",player)

    def test_reads_from_input_for_difficulty(self):
        difficulty = self.parser.difficulty()
        self.assertEqual("juggernaut",difficulty)
