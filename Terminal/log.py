from Terminal.constants import *
from Terminal import datetime, os


class Log:

    def __init__(self):
        self.storage = None
        self.save = None
        self.__setup__()

    def __setup__(self):
        savename = datetime.now().strftime("%y-%m-%d-%H-%M")
        dir = os.curdir
        if not os.path.exists(dir + LOGPATH):
            os.makedirs(dir + LOGPATH)

        savename = dir + LOGPATH + savename

        self.storage = open(TEMPFILE, 'w+')
        self.storage.close()
        self.storage = open(TEMPFILE, 'r+')

        if SAVELOG:
            self.save = open(savename+'.txt', 'w+')

    def write(self, text):
        if text[:-2] == '\n':
            self.storage.write(text)
        else:
            self.storage.write(text + '\n')

    def get(self):
        self.storage.seek(0)
        text = self.storage.readlines()
        self.clean()
        return text

    def clean(self):
        if SAVELOG:
            self.postcln()
        self.storage.seek(0)
        self.storage.truncate()

    def postcln(self):
        self.storage.seek(0)
        text = self.storage.readlines()
        for line in text:
            self.save.write(line)

    def close(self):
        self.storage.close()
        if SAVELOG:
            self.save.close()
        os.remove(TEMPFILE)
