import unittest

from game import Game
from prompter import Prompter
from user_interface import *
from test_utils import *

class UserInterfaceGameSetupTests(unittest.TestCase):
  
    def test_it_collects_user_input(self):
        user_input = MockUserInput(["stuff"])
        printer = FakePrinter()
        prompter = MockPrompter(printer,user_input)
        store = MockStore()
        interface = UserInterface(prompter,store)
        self.assertEqual({"insert random prompt here":"stuff"},interface.collected_data())

    def test_it_gets_prompter_and_store(self):
        user_input = MockUserInput(["stuff","more stuff"])
        printer = FakePrinter()
        prompter = MockPrompter(printer,user_input)
        store = MockStore()
        interface = UserInterface(prompter,store)
        fake_prompt = "insert random prompt here"
        self.assertTrue("Mock Prompter Present!" in printer.history_string())
        self.assertEqual({fake_prompt:"stuff"},interface.collected_data())

