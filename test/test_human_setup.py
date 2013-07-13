import unittest
from human_setup import HumanSetup

class HumanSetupTests(unittest.TestCase):

    def setUp(self):
        self.token_prompt = ("Would you like to play as x or o: ")
        self.difficulty_prompt = ("Would you like to play against an easy or impossible ai: ")
        self.order_prompt = ("Would you like to move first or second (1,2): ")
    
    def test_setup_human_token(self):
        user_data = {self.token_prompt:"x"}
        self.assertEqual("x",HumanSetup(user_data).human_token())

    def test_setup_human_token_with_empty(self):
        self.assertEqual(-1,HumanSetup({}).human_token())

    def test_setup_ai_token(self):
        user_data = {self.token_prompt:"x"}
        self.assertEqual("o",HumanSetup(user_data).opp_token())

    def test_setup_ai_token_with_o(self):
        user_data = {self.token_prompt:"o"} 
        self.assertEqual("x",HumanSetup(user_data).opp_token())

    def test_setup_ai_token_with_empty(self):
        user_data = {}
        self.assertEqual(-1,HumanSetup(user_data).opp_token())

    def test_user_first_with_1(self):
        user_data = {self.order_prompt:1}
        self.assertTrue(HumanSetup(user_data).user_first())

    def test_user_first_with_2(self):
        user_data = {self.order_prompt:2}
        self.assertFalse(HumanSetup(user_data).user_first())

    def test_difficulty_with_easy(self):
        user_data =  {self.difficulty_prompt:"easy"}
        self.assertEqual("easy",HumanSetup(user_data).difficulty())

    def test_difficulty_with_hard(self):
        user_data = {self.difficulty_prompt:"impossible"}
        self.assertEqual("impossible",HumanSetup(user_data).difficulty())

    def test_difficulty_with_empty(self):
        self.assertEqual(-1,HumanSetup({}).difficulty())



    

