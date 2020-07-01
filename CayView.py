from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
chromeDriverPath = "/Users/conghoang/.wdm/drivers/chromedriver/mac64/83.0.4103.39/chromedriver";

driver1 = webdriver.Chrome(chromeDriverPath)
driver1.get("https://www.google.com/")

driver2 = webdriver.Chrome(chromeDriverPath)
driver2.get("https://www.google.com/")