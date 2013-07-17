from user_interface import UserInterface
from game_builder import GameBuilder
from prompt_parser import PromptParser

if __name__ == "__main__":
    user_interface = UserInterface()
    parser = PromptParser(user_interface.collected_data)
    game = GameBuilder.game(parser)
    game.run()
