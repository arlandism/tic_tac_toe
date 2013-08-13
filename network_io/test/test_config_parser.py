import unittest
from config_parser import ConfigParser

class ConfigParserTests(unittest.TestCase):

    def test_instantiation(self):
        parser = ConfigParser("config.txt")
