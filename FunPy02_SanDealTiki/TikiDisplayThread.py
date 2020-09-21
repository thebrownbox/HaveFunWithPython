from threading import Thread
from TikiHunterThread import TikiHunterThread
import time
from os import system
from sys import platform

class TikiDisplayThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.hunters = []
        self.index = 0
    
    def addHunter(self, hunter):
        self.hunters.append(hunter)

    def show(self):
        for h in self.hunters:
            if(h.bestItem != None):
                print(h.bestItem.info())
                print("----------------")

    def isAllAlive(self):
        for h in self.hunters:
            if h.isAlive() == False:
                return False
        return True

    def run(self):
        while True and self.isAllAlive():
            self.index = (self.index + 1) % 100
            print("index: " + str(self.index))
            self.show()
            time.sleep(3)
            if platform == "win32": # for Windows
                system("cls")
            else:                   # for others
                system("clear")