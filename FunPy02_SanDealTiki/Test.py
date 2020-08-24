import requests
from bs4 import BeautifulSoup

URL = "https://tiki.vn/search?q=Apple%20AirPods%202&_lc=Vk4wMzQwMjcwMDM=&headphone_type=108271"
 
req = requests.get(URL)
file = open("template.html", "w+")
file.writelines(req.text)
file.close()
soup = BeautifulSoup(req.text, "lxml")