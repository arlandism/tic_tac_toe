from io.user_interface import UserInterface
from game.game_builder import GameBuilder
from io.prompt_parser import PromptParser
from io.prompter import Prompter
from io.speech_output import AudioOutput
from  game.board_speech_formatter import BoardSpeechFormatter
import getopt   
import sys

def say_flag_present(args):
    return args and args[0][0] == "-s"

def build_prompter(args,board_size=3):
    if say_flag_present(args):
        formatter = BoardSpeechFormatter(board_size) 
        return Prompter(display_object=AudioOutput(formatter))
    return Prompter()

if __name__ == "__main__":
    args, options = getopt.getopt(sys.argv[1:],"s")
    ui_prompter = build_prompter(args)
    user_interface = UserInterface(ui_prompter)
    parser = PromptParser(user_interface.collected_data())
    prompter = build_prompter(args,parser.board_size())
    game = GameBuilder.game(parser,prompter)
    game.run()

    
