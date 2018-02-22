from Terminal import Cmd
from Terminal.log import Log
from Terminal.constants import *
from Programs import program as PROGRAMS
import importlib


class Command(Cmd, Log):

    prompt = CMD
    nohelp = "No help on '%s'"

    def __init__(self):
        Log.__init__(self)
        Cmd.__init__(self, stdout=self.storage)
        # Cmd.__init__(self)

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

    def do_programs(self, args):
        """Lists all downloaded programs."""
        methods = []
        temp = []

        if args:
            for file in PROGRAMS:
                m = importlib.import_module(PROGRAM_PATH + file)
                temp = dir(m)
            for method in temp:
                if method[:3] == 'do_':
                    methods.append(method[3:])
            self.print_topics(PROGRAM_HEAD, methods, 15, 80)
        else:
            self.print_topics(PROGRAM_HEAD, PROGRAMS, 15, 80)

    def default(self, line):
        self.unknown(line)

    def unknown(self, command=None, args=None):
        if command:
            self.write("Unknown Command: " + "'" + command + "'")
        elif args:
            self.write("Unknown Argument: " + "'" + args + "'")
        else:
            self.write("Unknown")

    def cmd(self, line):
        self.onecmd(line)
        return self.postcmd()

    def onecmd(self, line) -> 'Re-writen to allow for custom programs and automatic importing':
        cmd, arg, line = self.parseline(line)
        if not line:
            return self.emptyline()
        if cmd is None:
            return self.default(line)
        self.lastcmd = line
        if line == 'EOF' :
            self.lastcmd = ''
        if cmd == '':
            return self.default(line)
        else:
            for file in PROGRAMS:
                f = importlib.import_module(PROGRAM_PATH + file)
                try:
                    func = getattr(f, 'do_' + cmd)
                    return func(self, arg)
                except AttributeError:
                    pass
            try:
                func = getattr(self, 'do_' + cmd)
            except AttributeError:
                return self.default(line)
            return func(arg)

    def postcmd(self, stop=None, line=None):
        super(Command, self).postcmd(stop, line)
        return self.get()
