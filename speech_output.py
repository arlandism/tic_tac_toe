import os
from board_speech_formatter import BoardSpeechFormatter

class AudioOutput(object):

    def __init__(self,speech_formatter=None,wpm=120):
        if speech_formatter is None:  speech_formatter=BoardSpeechFormatter(3)
        self.speech_formatter = speech_formatter
        self.wpm = wpm

    def display(self,x):
        print x
        formatted = self.speech_formatter.format_for_speech(x)
        os.system("say %s --rate=%s" % (formatted,self.wpm))
