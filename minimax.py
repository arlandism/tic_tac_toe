
class Minimax(object):

  PLAYERS_DICT = {'x':'o','o':'x'}

  def __init__(self,token,max_depth):
      self.token = token
      self.opponent_token = self.PLAYERS_DICT[self.token]
      self.minimax_status = {"alpha":-1,"beta":1}
      self.MAX_DEPTH = max_depth

  def next_move(self,board):
      if board.state() == {}:
          return board.keys[-1] 
      score_and_move_list = self.__build_score_and_move_list__(board)
      if score_and_move_list:
          best_score_and_move_list = max(score_and_move_list)
	  MOVE_INDEX = -1
          best_move = best_score_and_move_list[MOVE_INDEX] 
          return best_move

  def __build_score_and_move_list__(self,board):
      possible_moves = board.available_moves()
      move_list = [(self.__best_score__(move,board,self.token),move) for move in possible_moves]
      return move_list

  def __best_score__(self, space, board, player, depth=1):
      try:
          board.make_move(space,player)
	  if board.over() or depth == self.MAX_DEPTH: 
              return ((self.__cost_function__(board.winner()) * self.MAX_DEPTH) / depth)
          return self.__alpha_beta_prune__(board, player,depth)
      finally:
          board.erase_move(space)

  def __alpha_beta_prune__(self, board, player,depth):
      next_player = self.PLAYERS_DICT[player]
      if self.__comp_turn__(player):
          return self.__return_beta__(board,next_player,depth)
      else:
          return self.__return_alpha__(board,next_player,depth)

  def __return_beta__(self,board,next_player,depth):
      beta = self.minimax_status["beta"] 
      alpha = self.minimax_status["alpha"]
      possible_moves = board.available_moves()
      for move in possible_moves:
          beta = min(beta, self.__best_score__(move,board,next_player,depth+1))
          if beta <= alpha:
              break
      return beta

  def __return_alpha__(self,board,next_player,depth):
      alpha = self.minimax_status["alpha"]
      beta = self.minimax_status["beta"]
      possible_moves = board.available_moves()
      for move in possible_moves:
          alpha = max(alpha,self.__best_score__(move,board,next_player,depth+1))
          if beta <= alpha:
              break
      return alpha

  def __cost_function__(self, winner):
      cost_dict = {self.opponent_token:-1, self.token:1, None:0}
      return cost_dict[winner]

  def __comp_turn__(self, current_player):
      return current_player == self.token
