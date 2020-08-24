from threading import Thread
from Target import Target
from os import system, name
import time

def getItems(fileName):
    inputFile = open(fileName, "r")
    lines = inputFile.readlines()
    inputFile.close()
    
    lineCount = len(lines)
    listItem = []

    i = 0
    while (i+2) < lineCount:
        # print(lines[i])
        if(len(lines) == 0):
            break
        item = Target(lines[i].strip(), lines[i+1].strip(), lines[i+2].strip())
        listItem.append(item)
        i += 3

    return listItem


class Display(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.listHunter = []
    
    def addHunter(self, hunter):
        self.listHunter.append(hunter)

    def display(self):
        for hunter in self.listHunter:
            print(hunter.name + ": " + hunter.status)

    def isRuning(self):
        bIsRunning = False
        for hunter in self.listHunter:
            bIsRunning |= hunter.is_alive()
        return bIsRunning
    
    def run(self):
        while self.isRuning():
            self.display()
            time.sleep(0.5)
            system("clear")
        self.display()