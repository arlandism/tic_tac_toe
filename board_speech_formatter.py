class RowFormatter(object):

    def space_out(self,row):
        with_empties_spaced = row.replace("empty"," empty ")
        with_x_spaced = with_empties_spaced.replace("x"," x ")
        with_o_spaced = with_x_spaced.replace("o"," o ")
        left_spacing_removed = with_o_spaced.lstrip(" ")
        right_spacing_removed = left_spacing_removed.rstrip(" ")
        return right_spacing_removed 
    
    def pad_row(self,index,row):
        if len(row) == 0:
            return index * " "
        if len(row) == index:
            return row
        else:
            return row + (index - len(row)) * " "

    def replace_with_empty(self,row_string):
        return row_string.replace(" ","empty")

class BoardSpeechFormatter(object):

    def __init__(self,index):
        self.index = index

    def format_for_speech(self,string):
        trimmed = self.trim_board(string)
        board_rows = self.rows(trimmed)
        padded_rows = [RowFormatter().pad_row(self.index,row) for row in board_rows]
        empties_added = [RowFormatter().replace_with_empty(row) for row in padded_rows]
        spaced = [RowFormatter().space_out(row) for row in empties_added]
        row_nums_added = self.add_rows(spaced)
        return row_nums_added 

    def rows(self,board):
        row_list = []
        for row in range(self.index):
            start_of_row = row * self.index
            end_of_row = row * self.index + self.index
            row = board[start_of_row:end_of_row]
            row_list.append(row)
        return row_list

    def trim_board(self,board_string):
        no_dashes_or_newlines = filter(lambda x: x != "-" and x != "\n",board_string)
        trimmed_whitespace = no_dashes_or_newlines.replace("   "," ")
        trimmed_x = trimmed_whitespace.replace("  x","x")
        trimmed_o = trimmed_x.replace("  o","o")
        return trimmed_o

    def add_rows(self,rows):
        string = []
        for row_num in range(self.index):
            string.append(" row %s " % (row_num+1))
            string.append(rows[row_num])
        return "".join(string)

