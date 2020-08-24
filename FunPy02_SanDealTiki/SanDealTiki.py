# import Item as it
from Item import Item
from threading import Thread
from DealHunter import DealHunter
import Helper
import time

INPUT_FILE = "items_25.txt"

listItem = Helper.getItems(INPUT_FILE)




# for item in listItem:
    # item.info()
    # DealHunter(item).info()

def main():
    t1 = DealHunter(1, "AAAAAAAAAAAA")
    t2 = DealHunter(2, "------------")

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

if __name__ == '__main__':
    main()