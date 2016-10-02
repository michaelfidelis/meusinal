# thread_test.py
import threading
import time
###########################################################################-------------------------
class Monitor(threading.Thread):

    mon = [0]
    mon[0] = 3
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self.mon[0] == 2:
                print "Mon = 2"
                self.mon[0] = 3;
