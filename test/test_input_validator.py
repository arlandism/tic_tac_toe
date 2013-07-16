import unittest
from test_utils import MockUserInput
from playerinput import InputValidator

class InputValidatorTests(unittest.TestCase):

  def test_that_it_returns_a_str(self):
      valid_response = ("a","b")
      input_source = MockUserInput([7,"c","a"])
      self.assertEqual("a",InputValidator.return_valid_response(input_source,valid_response))

  def test_that_it_can_convert_types(self):
      valid_responses = ("2")
      input_source = MockUserInput([7,"c","a",2])
      self.assertEqual("2",InputValidator.return_valid_response(input_source,valid_responses))

  def test_that_it_can_return_int(self):
      valid_responses = (1,2,3)
      input_source = MockUserInput(["a","b",7,2])
      self.assertEqual(2,InputValidator.return_valid_response(input_source,valid_responses))

  def test_it_allows_quit(self):
      input_source = MockUserInput(["quit"])
      function = InputValidator.return_valid_response
      arg_one = input_source
      arg_two = "this test should exit"
      self.assertRaises(SystemExit,function,arg_one,arg_two)
