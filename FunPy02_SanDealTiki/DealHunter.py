from threading import Thread
import time

from Item import Item

class DealHunter (Thread):

    def __init__(self, id, name):
        Thread.__init__(self)
        self.threadID = id
        self.name = name

    def start(self):
        print("Thread " + self.name + " is started!")

    def run(self):
        count = 1000000
        while (count > 0):
            count -= 1
            print(count)
