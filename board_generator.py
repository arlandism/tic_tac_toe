
class BoardStringGenerator(object):

    def __init__(self,index,state=None):
        self.index = index
        self.cells = [cell for cell in range(1,self.index * self.index+1)]
        if state is None:  state = {}
        self.state = state
      
    def generate_layout(self):
        keys_present = self.state.keys()
        keys_not_present = set(self.cells) - set(keys_present)
        layout = dict()
        for key in keys_present:
            layout[str(key)] = self.state[key]
        for key in keys_not_present:
             layout[str(key)] = ""
        return layout

    def generate_template(self):
        board_template = []
        spaces_per_token = 3
        dashes = "-" * (spaces_per_token * self.index)
        left_side = "%("
        right_side = ")3s"
        for number in self.cells:
          if number % self.index == 0:
              board_template.append(left_side + str(number) + right_side + "\n" + dashes + "\n")
          else:
              board_template.append(left_side + str(number) + right_side)
        board_template = "".join(board_template)
        return board_template.rstrip("\n" + dashes) 

    def example_board(self):
        num_keys = (self.index * self.index) + 1
        dictionary = {}
        for key in range(1,num_keys):
            dictionary[str(key)] = key
        return self.generate_template() % dictionary
