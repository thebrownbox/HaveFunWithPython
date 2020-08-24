from threading import Thread
import time
import random


from Target import Target

class DealHunter (Thread):
    DELAY_TIME = 0.2
    LOOP_COUNT = 10

    def __init__(self, targetItem):
        Thread.__init__(self)
        self.item = targetItem
        self.name = self.item.name
        self.foundUrl = ""
        self.status = "...INIT..."


    def start(self):
        # print("=== [" + self.name + "] STARTED ===")
        self.status = "...STARTED..."
        return super().start()


    def run(self):
        i = 0
        self.status = "...RUNNING..."
        while True:
            i += 1
            # print(self.name + " - " + str(i))
            # time.sleep(random.random())
            time.sleep(DealHunter.DELAY_TIME)
            if i > random.randrange(10, 30): #DealHunter.LOOP_COUNT
                break
        # print("=== [" + self.name +"] FINISHED ===")
        self.foundUrl = "...FINISHED..."
        self.status = self.foundUrl
