import unittest
from game.board_generator import BoardStringGenerator

class BoardStringGeneratorTests(unittest.TestCase):

    def test_board_string_with_rows(self):
       	state = {1:"A"}
        generator = BoardStringGenerator(2,state)
        expected_layout = {"1":"A","2":"","3":"","4":""}
        self.assertEqual(expected_layout,generator.generate_layout())

    def test_board_string_with_all_emptys(self):
        state = {}
        generator = BoardStringGenerator(3,state)
        expected_layout = {'1':"",'2':"",'3':"",
                           '4':"",'5':"",'6':"",
                           '7':"",'8':"",'9':""}
        self.assertEqual(expected_layout,generator.generate_layout())

    def test_board_string_with_fours_board(self):
        state = {}
        keys = [str(i) for i in range(1,17)]
        generator = BoardStringGenerator(4,state)
        expected_layout = {}
        for key in keys:
            expected_layout[key] = ""
        self.assertEqual(expected_layout,generator.generate_layout())

class BoardTemplateGeneratorTests(unittest.TestCase):

    def test_template_with_fours(self):
        row_one = "%(1)3s%(2)3s%(3)3s%(4)3s\n"
        row_two = "\n%(5)3s%(6)3s%(7)3s%(8)3s\n"
        equal_signs = "=" * 12
        row_three = "\n%(9)3s%(10)3s%(11)3s%(12)3s\n"
        row_four = "\n%(13)3s%(14)3s%(15)3s%(16)3s"
        board_template = row_one + equal_signs +  row_two + equal_signs +  row_three + equal_signs + row_four
        generator = BoardStringGenerator(4, {})
        self.assertEqual(board_template,generator.generate_template())

    def test_template_with_threes(self):
        row_one = "%(1)3s%(2)3s%(3)3s\n"
        row_two = "\n%(4)3s%(5)3s%(6)3s\n"
        row_three = "\n%(7)3s%(8)3s%(9)3s"
        equal_signs = "=" * 9
        board_template = row_one + equal_signs + row_two + equal_signs + row_three 
        generator = BoardStringGenerator(3,{})
        self.assertEqual(board_template,generator.generate_template())

class BoardTemplateExampleBoardTests(unittest.TestCase):
   
    def test_example_board_with_threes_board(self):
        example_board = ("  1  2  3\n=========\n  4  5  6\n=========\n  7  8  9")
        self.assertEqual(example_board,BoardStringGenerator(3).example_board())

