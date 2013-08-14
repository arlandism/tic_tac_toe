import unittest
from config_parser import ConfigParser

class ConfigParserTests(unittest.TestCase):

    fake_config_file = ("first_token: test_token\n" +
                        "second_token: test_token_two\n" +
                        "player_one: test_player_one\n" +
                        "player_two: test_player_two\n" +
                        "depthlimit: 100\n"+
                        "board_size: 4\n")

    def setUp(self):
        self.parser = ConfigParser(self.fake_config_file)
        self.parser_with_blank_file = ConfigParser("")

    def test_reads_from_input_for_token_or_defaults(self):
        token = self.parser.first_token()
        self.assertEqual("test_token",token)
        parser = self.parser_with_blank_file
        self.assertEqual("x", parser.first_token())
        
    def test_reads_from_input_for_player_one_or_defaults(self):
        self.assertEqual("test_player_one",self.parser.player_one())
        default = self.parser_with_blank_file.player_one()
        self.assertEqual("Human", default)
        
    def test_reads_from_input_for_player_two_or_defaults(self):
        self.assertEqual("test_player_two",self.parser.player_two())
        default = self.parser_with_blank_file.player_two()
        self.assertEqual("ImpossibleAI", default)

    def test_reads_from_input_for_difficulty_or_defaults(self):
        difficulty = self.parser.difficulty()
        self.assertEqual(100,difficulty)
        default = self.parser_with_blank_file.difficulty()
        self.assertEqual(20,default)

    def test_reads_from_input_for_board_size_or_defaults(self):
        self.assertEqual(4, self.parser.board_size())
        default = self.parser_with_blank_file.board_size()
        self.assertEqual(3, default)
