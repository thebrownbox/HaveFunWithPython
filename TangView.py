import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

cssSelectorBtPlay = "#movie_player > div.ytp-cued-thumbnail-overlay > button"
fileName = "videolist.txt"

myFile = open(fileName)
listUrl = myFile.readlines()

url = "https://www.youtube.com/watch?v=9EqZrpEs5rw"

url2 = "https://www.youtube.com/watch?v=VIHXxOWeszQ"

browser = webdriver.Chrome()
browser.get(url)
time.sleep(1)
browser.set_window_position(100,100);
e = browser.find_element_by_css_selector(cssSelectorBtPlay)
e.click()
print (browser.current_window_handle)

time.sleep(2)
browser.execute_script("window.open('"+url2+"')")

time.sleep(2)
browser.execute_script("window.open('"+url2+"')")

time.sleep(2)
browser.execute_script("window.open('"+url2+"')")

time.sleep(2)
browser.execute_script("window.open('"+url2+"')")

time.sleep(2)
print (browser.current_window_handle)



count = 0;
while True:
    count = (count + 1) % 4;
    browser.switch_to.window(browser.window_handles[count])
    time.sleep(0.5)
    browser.get(listUrl[count])
    time.sleep(2);
