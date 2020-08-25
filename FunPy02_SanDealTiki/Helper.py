from threading import Thread
from Target import Target
from Item import Item
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
        item = Target(lines[i].strip(), correctNumber(lines[i+1].strip()), lines[i+2].strip())
        listItem.append(item)
        i += 3

    return listItem

def correctNumber(strPrice):
    strPrice = strPrice.replace('.', '')
    strPrice = strPrice.replace('đ', '')
    return int(strPrice)

def numberToStrPrice(intPrice):
    strPrice = str(intPrice)
    n = len(strPrice)
    k = int((n-1) / 3)
    # print("k = " + str(k) + " n = " + str(n))
    i = 0
    while i < k:
        i += 1
        index = (-3) * i - (i-1)
        strPrice = strPrice[:index] + "." + strPrice[index:]
    return strPrice

def getItemFromHtmlElement(itemHtml):
    newItem = Item()
    # 1. Get title
    newItem.name = itemHtml.get("title")
    # 2. Get final price
    priceText = itemHtml.find("span", {"class":"final-price"}).get_text()
    # 3. Get regular price (If has)
    regularPrice = itemHtml.find("span", {"class":"price-regular"})
    if(regularPrice != None):
        newItem.regularPrice = correctNumber(regularPrice.get_text().strip())

        finalPrice = str(priceText).split("đ")
        if(len(finalPrice) > 0): # discount if has
            newItem.price = correctNumber(finalPrice[0].strip())
            newItem.discount = finalPrice[1].strip()
    else:
        newItem.price = correctNumber(priceText)
        newItem.regularPrice = 0
        newItem.discount = ""

    # 4. url
    url = "https://tiki.vn" + itemHtml.get("href")
    newItem.url = url
    return newItem


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
        pass