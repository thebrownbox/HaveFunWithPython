from threading import Thread
from Helper import getItemFromHtmlElement
from Helper import numberToStrPrice
import time
import random
import requests
from bs4 import BeautifulSoup

from Target import Target

class DealHunter (Thread):
    DELAY_TIME = 3

    def __init__(self, targetItem):
        Thread.__init__(self)
        self.target = targetItem
        self.name = self.target.name + "("+numberToStrPrice(self.target.maxPrice)+")"
        self.display = "...INIT..."


    def start(self):
        # print("=== [" + self.name + "] STARTED ===")
        self.display = "...STARTED..."
        return super().start()

    def findTheBestDeal(self):
        req = requests.get(self.target.url)
        soup = BeautifulSoup(req.text, "lxml")
        htmlElements = soup.findAll("a", {"class": "search-a-product-item"})
        
        listItem = []
        for htmlElement in htmlElements:
            newItem = getItemFromHtmlElement(htmlElement)
            if newItem != None:
                if (self.target.name in newItem.name) and (newItem.price < self.target.maxPrice):
                    listItem.append(newItem)
        
        if len(listItem) > 0:
            self.display = ""
            # print(self.target.name + " ("  + numberToStrPrice(self.target.maxPrice) + "): " + ": " + str(len(listItem)) + " items:")
            self.display += (self.name + ": " + str(len(listItem)) + " items:") + "\n"
            i = 1
            for item in listItem:
                # print(str(i)+", "+numberToStrPrice(item.price) +": " + item.url)
                self.display += (str(i)+", "+numberToStrPrice(item.price) +": \n" + item.url) + "\n"
                i += 1
        else:
            self.display = self.name +": ...RUNNING..." + "\n"

    def run(self):
        i = 0
        self.display = self.name + ": ...RUNNING..." + "\n"
        # print(self.target.name +": RUNNING...")
        while True:
            self.findTheBestDeal()
            time.sleep(DealHunter.DELAY_TIME)

        self.display = "...FINISHED..." + "\n"
