from user_interface import UserInterface
from game_builder import GameBuilder
from prompt_parser import PromptParser
from prompter import Prompter
from speech_output import AudioOutput
import getopt   
import sys

if __name__ == "__main__":
    args, options = getopt.getopt(sys.argv[1:],"s")
    if args and args[0][0] == "-s":
        prompter = Prompter(display_object=AudioOutput())
    else:
        prompter = Prompter()
    user_interface = UserInterface(prompter)
    parser = PromptParser(user_interface.collected_data())
    game = GameBuilder.game(parser,prompter)
    game.run()
