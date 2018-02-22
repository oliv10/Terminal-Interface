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

        if args:
            methods = []
            temp = []
            for file in PROGRAMS:
                m = importlib.import_module(PROGRAM_PATH + file)
                temp = dir(m)
            for method in temp:
                if method[:3] == 'do_':
                    methods.append(method[3:])
            self.print_topics(PROGRAM_HEAD[0], methods, 15, 80)
        else:
            pro_builtin = []
            pro_download = []
            pro_unknown = []

            for file in PROGRAMS:
                f = importlib.import_module(PROGRAM_PATH + file)
                attr = None
                try:
                    attr = getattr(f, ATTR)
                except AttributeError:
                    pro_unknown.append(file)
                if attr == 1:
                    pro_builtin.append(file)
                elif attr == 2:
                    pro_download.append(file)
                else:
                    pass

            self.print_topics(PROGRAM_HEAD[1], pro_builtin, 15, 80)
            self.print_topics(PROGRAM_HEAD[2], pro_download, 15, 80)
            self.print_topics(PROGRAM_HEAD[3], pro_unknown, 15, 80)

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

    def onecmd(self, line) -> 'Re-writen to allow for custom programs and automatic importing.':
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
        
    def do_help(self, arg) -> 'Re-written to allow to custom programs and automatic helping.':
        """List available commands with "help" or detailed help with "help cmd"."""
        if arg:
            for file in PROGRAMS:
                f = importlib.import_module(PROGRAM_PATH + file)
                try:
                    func = getattr(f, 'help_' + arg)
                except AttributeError:
                    try:
                        doc = getattr(f, 'do_' + arg).__doc__
                        if doc:
                            self.write("%s\n" % str(doc))
                            return
                    except AttributeError:
                        pass
                    super(Command, self).do_help(arg)

    def postcmd(self, stop=None, line=None) -> 'Re-written to allow for responses to be returned properly.':
        super(Command, self).postcmd(stop, line)
        return self.get()
