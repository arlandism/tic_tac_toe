import unittest
from human_prompt_interface import HumanPromptInterface

class HumanPromptInterfaceFlagsTests(unittest.TestCase):

    def test_that_it_returns_supplied_prompts_and_responses(self):
	another_prompt = {"Supply a letter": ("a","b","c")}
        prompts = HumanPromptInterface.prompts(another_prompt)
	self.assertTrue("a" in prompts["Supply a letter"])

    def test_interface_provides_response_choices_with_default_prompts(self):
	# Define defaults here in case we need to change them later
	defaults = {"Would you like to play as x or o: ":("x","o"),
		    "Would you like to move first or second (1,2): ":(1,2),
		    "Would you like to play against an easy or impossible ai: ":("easy","impossible")}
	prompts = HumanPromptInterface.prompts()
	for prompt,responses in defaults.items():
	    self.assertEqual(responses,prompts[prompt])

    def test_returned_hash_is_ordered(self):
	prompt = {"I'm a prompt":"second from last item"}
	new_prompt = {"random prompt":"latest item"}
	prompts = HumanPromptInterface.prompts(prompt,new_prompt)
	SECOND_FROM_LAST = -2
	self.assertEqual(prompts.values()[SECOND_FROM_LAST],"second from last item")
	LAST_ITEM = -1
	self.assertEqual(prompts.values()[LAST_ITEM],"latest item")
