from Target import Target
from threading import Thread
from DealHunter import DealHunter
import Helper
import time
import sys
import timeit

INPUT_FILE = "items_25.txt"

def main(fileName):
    # get data from file
    listItem = Helper.getItems(fileName)

    listThread = []

    # create display thread
    displayThread = Helper.Display()
    listThread.append(displayThread)
    
    # create hunter threads
    for item in listItem:
        hunter = DealHunter(item)
        
        listThread.append(hunter)
        displayThread.addHunter(hunter)

        hunter.start()

    displayThread.start()

    # join all thread
    for t in listThread:
        t.join()
    
if __name__ == '__main__':
    if(len(sys.argv) > 1):
        main(sys.argv[1])
    else:
        main(INPUT_FILE)