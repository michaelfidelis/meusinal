#! /usr/bin/python
import cv2
import numpy as np
from threading import Thread

class Teste(Thread):

    def __init__(self,low,high):
        super(Teste, self).__init__()
        self.low=low
        self.high=high
        self.total=0

    def run(self):
        for i in range(self.low,self.high):
            self.total+=i

thread1 = Teste(0,500000)
thread2 = Teste(500000,1000000)
thread1.start() # This actually causes the thread to run
thread2.start()
thread1.join() # This waits until the thread has completed
print thread2.total
thread2.join()
print thread2.total
# At this point, both threads have completed
result = thread1.total + thread2.total
print result
