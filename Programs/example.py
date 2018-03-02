ATTR = 1  # Tells the terminal where this program came from ex (Downloaded, Builtin, or Unknown if variable not found)


def do_add(self, args):  # This is the command that can be called from within the terminal #
    """Adds numbers together."""
    ans = 0
    if args:
        nums = args.split(' ')
        try:
            for n in nums:
                ans += int(n)
        except ValueError:
            self.write(ValueError.__name__)
            return
        self.write("Answer: " + str(ans))
