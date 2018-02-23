from threading import Thread
from datetime import datetime
import time

ATTR = 1
RUNNING = False
current_time = ""


""" This example uses a Threaded program, one which will constantly repeat 
a given function. In this example it is to continuously update the time. """


def __setup():
    global RUNNING
    RUNNING = True
    t = Thread(target=__update, name="Time")
    t.setDaemon(True)
    t.start()


def __update():
    global current_time
    while RUNNING:
        current_time = datetime.now()
        time.sleep(1)


def do_time(self, args):
    if not RUNNING:
        __setup()
    self.write("Time is: " + str(current_time))
