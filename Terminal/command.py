from Terminal import Cmd
from Terminal.log import Log
from Terminal.constants import *


class Command(Cmd, Log):

    prompt = CMD
    nohelp = "No help on '%s'"

    def __init__(self):
        Log.__init__(self)
        Cmd.__init__(self, stdout=self.storage)

    def do_quit(self, args):
        """Quits and shuts down the program."""
        if args:
            self.unknown(args=args)
        else:
            self.write("Quit by User")
            self.postcmd()
            Log.close(self)
            raise SystemExit

    def do_clear(self, args):
        """Clears the screen."""
        if args:
            self.unknown(args=args)
        else:
            self.write(CLEAR)

    def default(self, line):
        self.unknown(line)

    def unknown(self, command=None, args=None):
        if command:
            self.write("Unknown Command: " + "'" + command + "'")
        elif args:
            self.write("Unknown Argument: " + "'" + args + "'")
        else:
            self.write("Unknown")

    def onecmd(self, line):
        super(Command, self).onecmd(line)
        return self.postcmd()

    def postcmd(self, stop=None, line=None):
        super(Command, self).postcmd(stop, line)
        return self.get()
