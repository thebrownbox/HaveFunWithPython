# import Item as it
from Item import Item
from threading import Thread
from DealHunter import DealHunter
import Helper
import time
import sys
import timeit

INPUT_FILE = "items_25.txt"

def main(fileName):
    listItem = Helper.getItems(fileName)
    gang = []
    
    start = timeit.default_timer()
    for item in listItem:
        hunter = DealHunter(item)
        hunter.start()
        gang.append(hunter)
        # hunter.join()

    
    # time.sleep(3)
    for hunter in gang:
        hunter.join()
    
    start = timeit.default_timer() - start
    print("=========== "+ str(start) +" ==============")
    time.sleep(3)    
    print("============2=============")

if __name__ == '__main__':
    if(len(sys.argv) > 1):
        main(sys.argv[1])
    else:
        main(INPUT_FILE)