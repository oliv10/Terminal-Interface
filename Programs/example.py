def do_add(self, args):
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
