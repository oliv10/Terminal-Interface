from Terminal import *
from Terminal.constants import DEBUG


def debug():
    while True:
        get = input("Debug: ")
        if get == "threads":
            print(threading.enumerate())


if __name__ == '__main__':
    t = threading.Thread(target=terminal.Terminal, name="Terminal")
    t.setDaemon(False)
    t.start()
    if DEBUG:
        r = threading.Thread(target=debug, name="Debugging")
        r.setDaemon(True)
        r.start()
