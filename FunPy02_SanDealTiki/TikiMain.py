from TikiTarget import TikiTarget
from TikiItem import TikiItem
from TikiHunterThread import TikiHunterThread
from TikiDisplayThread import TikiDisplayThread
from TikiHelper import *
from bs4 import BeautifulSoup
import requests
import time

TARGET_FILE = "target_list.txt"

targets = getTargetsFromFile(TARGET_FILE)
threads = []
displayThread = TikiDisplayThread()

for t in targets:
    hunter = TikiHunterThread(t)
    hunter.start()
    threads.append(hunter)
    displayThread.addHunter(hunter)

displayThread.start()

for t in threads:
    t.join()

print ("===== END Main ====")