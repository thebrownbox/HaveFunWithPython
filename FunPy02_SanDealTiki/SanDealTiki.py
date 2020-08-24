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
    # t1 = DealHunter(1, "AAAAAAAAAAAA")
    # t2 = DealHunter(2, "------------")

    t1 = DealHunter()
    t2 = DealHunter()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

class MyThread(Thread):
    def run(self):
        time.sleep(5)
        return


if __name__ == '__main__':
    main()
    # for i in range(3):
    #     t = MyThread()
    #     t.start()
    #     print ('t.is_alive()=' + str(t.is_alive()))
    #     t.join()
    #     print ('t.is_alive()=' + str(t.is_alive()))