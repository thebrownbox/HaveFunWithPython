from threading import Thread
import time
import random
from os import system, name

from Item import Item

class DealHunter (Thread):
    DELAY_TIME = 0.2
    LOOP_COUNT = 10

    def __init__(self, targetItem):
        Thread.__init__(self)
        self.item = targetItem
        self.name = self.item.name


    def start(self):
        print("=== [" + self.name + "] STARTED ===")
        return super().start()


    def run(self):
        i = 0
        # time.sleep(1)
        while True:
            i += 1
            # system("clear")
            print(self.name + " - " + str(i))
            # time.sleep(random.random())
            time.sleep(DealHunter.DELAY_TIME)
            if i > DealHunter.LOOP_COUNT:
                break
        print("=== [" + self.name +"] FINISHED ===")
