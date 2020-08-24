from threading import Thread
from Helper import getItemFromHtmlElement
import time
import random
import requests
from bs4 import BeautifulSoup

from Target import Target

class DealHunter (Thread):
    DELAY_TIME = 10
    LOOP_COUNT = 10

    def __init__(self, targetItem):
        Thread.__init__(self)
        self.target = targetItem
        self.name = self.target.name
        self.status = "...INIT..."


    def start(self):
        # print("=== [" + self.name + "] STARTED ===")
        self.status = "...STARTED..."
        return super().start()

    def findTheBestDeal(self):
        req = requests.get(self.target.url)
        soup = BeautifulSoup(req.text, "lxml")
        htmlElements = soup.findAll("a", {"class": "search-a-product-item"})
        
        listItem = []
        for htmlElement in htmlElements:
            newItem = getItemFromHtmlElement(htmlElement)
            if self.target.name in newItem.name and newItem.price < self.target.maxPrice:
                listItem.append(newItem)

        print(self.target.name + ": " + str(len(listItem)) + " items:")
        for item in listItem:
            # print(self.target.name + ": " + str(item.price) + "\n" + item.url)
            print(self.target.name + ": " + str(item.price))

    def run(self):
        i = 0
        self.status = "...RUNNING..."
        while True:
            self.findTheBestDeal()
            time.sleep(DealHunter.DELAY_TIME)

        self.status = "...FINISHED..."
