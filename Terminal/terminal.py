from tkinter import *
from Terminal.constants import *
from Terminal.command import Command


class Terminal(Tk, Command):

    def __init__(self):
        Tk.__init__(self, className=' Terminal')
        Command.__init__(self)

        self.entry = Entry(self)
        self.text = Text(self)

        self.setup()
        self.mainloop()

    def setup(self):

        self.wm_minsize(WIDTH, HEIGHT)
        self.wm_maxsize(WIDTH, HEIGHT)

        self.entry.bind("<Key>", self.action)
        self.entry.configure(width=100)

        self.text.configure(background="black", foreground="white", state=DISABLED)

        label = Label(self, text=CMD)

        self.text.pack()
        label.pack(side=LEFT)
        self.entry.pack(side=LEFT)

    def update_text(self, text):
        self.text.configure(state=NORMAL)
        if text[0] == CLEAR:
            self.text.delete('1.0', END)
        else:
            for line in text:
                self.text.insert(INSERT, CMD + line)
        self.text.configure(state=DISABLED)
        self.text.update()

    def action(self, key):
        action = key.keycode
        if action == ENTER:
            text = Command.onecmd(self, self.entry.get())
            self.update_text(text)
            self.entry.delete(0, END)
