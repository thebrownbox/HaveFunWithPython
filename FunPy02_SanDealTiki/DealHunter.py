from threading import Thread
import time

from Item import Item

class DealHunter (Thread):

    # def __init__(self, id, name):
    #     Thread.__init__(self)
    #     self.threadID = id
    #     self.name = name

    # def start(self):
    #     print("Thread " + self.name + " is started!")

    def run(self):
        i = 0
        time.sleep(1)
        while True:
            i += 1
            print(self.name + " - " + str(i))
            if i > 100:
                break
