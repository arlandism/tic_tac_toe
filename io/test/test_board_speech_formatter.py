import unittest
from io.board_speech_formatter import BoardSpeechFormatter,RowFormatter,SpeechFormatter
from game.board_generator import BoardStringGenerator
from game.base_board import BaseBoard

class BoardSpeechFormatterTests(unittest.TestCase):

    def setUp(self):
        self.formatter = BoardSpeechFormatter(3)
        self.fours_formatter = BoardSpeechFormatter(4)

    def test_rows_with_one_row(self):
        board = "xox"
        expected = ["xox","",""]
        self.assertEqual(expected,self.formatter.rows(board))

    def test_rows_with_two_rows(self):
        board = "xoxx"
        expected = ["xox","x",""]
        self.assertEqual(expected,self.formatter.rows(board))

    def test_rows_with_three_rows(self):
        board = "ooxxooo"
        expected = ["oox", "xoo","o"]
        self.assertEqual(expected,self.formatter.rows(board))

    def test_rows_with_full_board(self):
        board = "oooxoxoxx"
        expected = ["ooo","xox","oxx"]
        self.assertEqual(expected,self.formatter.rows(board))

    def test_rows_with_fours_board(self):
        board = "xxoooxxooxxxooo"
        expected = ["xxoo","oxxo","oxxx","ooo"]
        self.assertEqual(expected,self.fours_formatter.rows(board))

    def test_rows_with_empty_spaces_between(self):
        board = "xox x"
        expected = ["xox", " x", ""]
        self.assertEqual(expected,self.formatter.rows(board))

    def test_rows_with_all_empties(self):
        board = ""
        expected = ["","",""]
        self.assertEqual(expected,self.formatter.rows(board))

    def test_rows_with_empties_at_beginning(self):
        board = " xox"
        expected = [" xo","x  ",""]

    def test_trim_board(self):
        board = BaseBoard(3)
        board.make_move(4,"x")
        board.make_move(9,"o")
        board_string = board.__str__()
        expected = "   x    o"
        self.assertEqual(expected,self.formatter.trim_board(board_string))

    def test_add_rows(self):
        rows = [" x x x "," empty empty empty "," o x x "]
        expected = " row 1  x x x  row 2  empty empty empty  row 3  o x x "
        self.assertEqual(expected,self.formatter.add_rows(rows))

    def test_format_for_speech(self):
        board = BaseBoard(3)
        board.board_state = {1:"x", 8:"o", 9:"x"}
        board_string = board.__str__()
        row_one = " row 1 x  empty  empty"
        row_two = " row 2 empty  empty  empty"
        row_three = " row 3 empty  o  x"
        expected = (row_one + row_two + row_three)
        self.assertEqual(expected,self.formatter.format_for_speech(board_string))

    def test_format_for_speech_with_fours_board(self):
        board = BaseBoard(4)
        board.board_state = {1:"x", 8:"o", 9:"x"}
        board_string = board.__str__()
        row_one = " row 1 x  empty  empty  empty"
        row_two = " row 2 empty  empty  empty  o"
        row_three = " row 3 x  empty  empty  empty"
        row_four = " row 4 empty  empty  empty  empty"
        expected = (row_one + row_two + row_three + row_four)
        self.assertTrue(self.fours_formatter.is_board_string(board_string))
        self.assertEqual(expected,self.fours_formatter.format_for_speech(board_string))

    def test_it_knows_board_string(self):
        board_string = BoardStringGenerator(3).generate_template()
        self.assertTrue(self.formatter.is_board_string(board_string))

    def test_it_knows_fours_board_string(self):
        board_string = BoardStringGenerator(4).generate_template()
        self.assertTrue(self.formatter.is_board_string(board_string))

    def test_it_knows_non_board_string(self):
        non_board_string = "X's turn"
        self.assertFalse(self.formatter.is_board_string(non_board_string))

class SpeechFormatterTests(unittest.TestCase):
 
    def test_it_can_format_regular_strings(self):
        reg_string = "whatup\n\n==="
        self.assertEqual("whatup",SpeechFormatter.format_regular(reg_string))
        

class RowFormatterTests(unittest.TestCase):

    def setUp(self):
        self.formatter = RowFormatter()

    def test_pad_row_with_one_empty(self):
        row = " x"
        padded = " x "
        self.assertPadded(padded,row)

    def test_pad_row_with_two_empties(self):
        row = "  x"
        padded = "  x"
        self.assertPadded(padded,row)

    def test_pad_with_three_empties(self):
        row = ""
        padded = "   "
        self.assertPadded(padded,row)

    def test_pad_with_full_row(self):
        row = "ooo"
        padded = "ooo"
        self.assertPadded(padded,row)

    def test_pad_with_diff_tokens(self):
        row = "xo"
        padded = "xo "
        self.assertPadded(padded,row)

    def test_pad_with_multiple_rows(self):
        board = "xox oo  o"
        rows = BoardSpeechFormatter(3).rows(board)
        expected_row_one = "xox"
        expected_row_two = " oo"
        expected_row_three = "  o" 
        self.assertPadded(expected_row_one, rows[0])
        self.assertPadded(expected_row_two, rows[1])
        self.assertPadded(expected_row_three, rows[2])

    def test_pad_with_fours_board(self):
        board = "xoo xx  xxxxo oo"
        rows = BoardSpeechFormatter(4).rows(board)
        expected_row_one = "xoo "
        expected_row_two = "xx  "
        expected_row_three = "xxxx"
        expected_row_four = "o oo"
        expected_rows = [expected_row_one, expected_row_two, 
                         expected_row_three, expected_row_four]
        for num in range(4):
            self.assertPadded(expected_rows[num],self.formatter.pad_row(4,rows[num]))

    def test_replace_with_empty(self):
        board = "xoo "
        expected = "xooempty"
        self.assertEqual(expected, self.formatter.replace_with_empty(board))

    def test_replace_with_empty_two_spaces(self):
        board = " xx "
        expected = "emptyxxempty"
        self.assertEqual(expected, self.formatter.replace_with_empty(board))

    def test_space_out(self):
        board = "emptyxxempty"
        expected = "empty  x  x  empty"
        self.assertEqual(expected, self.formatter.space_out(board))

    def assertPadded(self,padded,row):
        self.assertEqual(padded,self.formatter.pad_row(3,row))
