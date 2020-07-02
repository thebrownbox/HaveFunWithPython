from selenium import webdriver
from selenium.webdriver.common.keys import Keys

cssSelectorBtPlay = "#movie_player > div.ytp-cued-thumbnail-overlay > button"

url = "https://www.youtube.com/watch?v=9EqZrpEs5rw"

url2 = "https://www.youtube.com/watch?v=VIHXxOWeszQ"

driver1 = webdriver.Chrome()
driver1.set_window_size(100, 100)
driver1.set_window_position(0, 0)
driver1.get(url)
elem1 = driver1.find_element_by_css_selector(cssSelectorBtPlay)
elem1.click()
window1 = driver1.current_window_handle


driver2 = webdriver.Chrome()
driver2.set_window_size(100, 100);
driver2.set_window_position(driver1.get_window_size()['width'], 0)
driver2.get(url2)
elem2 = driver2.find_element_by_css_selector(cssSelectorBtPlay)
elem2.click()

window2 = driver2.current_window_handle
driver2.switch_to.window(driver2.window_handles[0])