from Terminal import Cmd
from Terminal.log import Log
from Terminal.constants import *
from Programs import program


class Command(Cmd, Log):

    prompt = CMD
    nohelp = "No help on '%s'"

    def __init__(self):
        Log.__init__(self)
        # Cmd.__init__(self, stdout=self.storage)
        Cmd.__init__(self)

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

    def cmd(self, line):
        self.onecmd(line)
        return self.postcmd()

    def onecmd(self, line) -> 'Re-writen to allow for custom programs':
        """Interpret the argument as though it had been typed in response
        to the prompt.

        This may be overridden, but should not normally need to be;
        see the precmd() and postcmd() methods for useful execution hooks.
        The return value is a flag indicating whether interpretation of
        commands by the interpreter should stop.

        """
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

            if len(program) > 0:
                for file in program:
                    try:
                        func = getattr(file, 'do_' + cmd)
                        return func(file, arg)
                    except AttributeError:
                        pass
            else:
                try:
                    func = getattr(self, 'do_' + cmd)
                    return func(self, arg)
                except AttributeError:
                    return self.default(line)

    def postcmd(self, stop=None, line=None):
        super(Command, self).postcmd(stop, line)
        return self.get()
