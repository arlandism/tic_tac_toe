import unittest

from io.board_speech_formatter import BoardSpeechFormatter, SpeechFormatter
from io.speech_output import AudioOutput

class AudioOutputTests(unittest.TestCase):

    def setUp(self):
        self.formatter = BoardSpeechFormatter(3)
        self.output = AudioOutput(self.formatter)

    def test_it_receives_speech_formatter(self):
        self.assertEqual(self.formatter,self.output.speech_formatter)

    def test_it_takes_wpm_arg(self):
        output = AudioOutput(self.formatter,60)
        self.assertEqual(60,output.wpm)
