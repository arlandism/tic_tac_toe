import os

class AudioOutput(object):

    def display(self,x):
        os.system("say %s" % x)
