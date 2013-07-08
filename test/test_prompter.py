import unittest
from prompter import *
from test_utils import FakePrinter,MockUserInput
from collections import OrderedDict

class PrompterTests(unittest.TestCase):

    def setUp(self):
	self.fake_printer = FakePrinter()
	mock = MockUserInput([" "] * 20)
	self.prompter = Prompter(self.fake_printer,mock)

    def test_prompter_shows_multiple_prompts(self):
	self.prompter.prompt_and_collect_input({"What's up":" ","Promptin you":" "})
	self.assertPromptWasShown("What's up")
	self.assertPromptWasShown("Promptin you")

    def test_prompter_retains_all_input(self):
	ui = MockUserInput(["dog","cat","bird"])
	prompter = Prompter(input_object=ui)
	prompt_dictionary = OrderedDict()
	prompt_dictionary["one"] = "dog"
	prompt_dictionary["two"] = "cat"
	prompt_dictionary["three"] = "bird"
	prompter.prompt_and_collect_input(prompt_dictionary)
	self.assertTrue("dog" in prompter.return_answers())
	self.assertTrue("cat" in prompter.return_answers())
	self.assertTrue("bird" in prompter.return_answers())

    def test_prompter_accepts_only_valid_input(self):
	ui = MockUserInput(["cheshire","rottweiler"])
	appropriate_responses = ["doberman","husky","rottweiler"]
	self.prompter.input_object=ui
	self.prompter.prompt_and_collect_input({"Name a dog breed": appropriate_responses})
	self.assertTrue("rottweiler" in self.prompter.return_answers())
   
    def test_prompter_returns_prompt_to_answer_hash(self):
	prompter = Prompter(input_object=MockUserInput(["some junk","input","here's more"]))
	prompts = OrderedDict()
	prompts["input something"] = ("input","other input")
	prompts["more..."] = ("here's more","more more")
	prompter.prompt_and_collect_input(prompts)
	answer_hash = prompter.return_answer_hash()
	
	self.assertEqual("input",answer_hash["input something"])

	self.assertEqual("here's more", answer_hash["more..."])
	
    def assertPromptWasShown(self,prompt):
        prompt_history = "".join(self.fake_printer.history)	
	self.assertTrue(prompt in prompt_history)
