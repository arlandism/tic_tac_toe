from user_interface import UserInterface
from game_builder import GameBuilder

if __name__ == "__main__":
    user_interface = UserInterface()
    game = GameBuilder.game(user_interface.collected_data())
    game.run()
