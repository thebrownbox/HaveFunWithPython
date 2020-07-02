import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

cssSelectorBtPlay = "#movie_player > div.ytp-cued-thumbnail-overlay > button"
fileName = "videolist.txt"

myFile = open(fileName)
listVideo = myFile.readlines()

NUMBER_OF_WINDOW = 4
NUMBER_OF_VIDEO = len(listVideo)

print("WINDOW: " + str(NUMBER_OF_WINDOW))
print("VIDEO: " + str(NUMBER_OF_VIDEO))

videoIndex = 0
windowIndex = 0
windowCount = 1

browser = webdriver.Chrome()
browser.get(listVideo[videoIndex])
browser.set_window_position(100,100);
time.sleep(1)
e = browser.find_element_by_css_selector(cssSelectorBtPlay)
e.click()


while True:
    videoIndex = (videoIndex + 1) % NUMBER_OF_VIDEO
    windowIndex = (windowIndex + 1) % NUMBER_OF_WINDOW
    print(str(windowIndex) + " : " + str(videoIndex))
    url = listVideo[videoIndex].strip();

    if windowCount < NUMBER_OF_WINDOW:
        windowCount = windowCount + 1;
        browser.execute_script("window.open('"+url+"')")
    else:
        browser.switch_to.window(browser.window_handles[windowIndex])
        time.sleep(0.5)
        browser.get(url)
    
    time.sleep(3)