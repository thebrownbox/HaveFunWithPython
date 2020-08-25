import requests
from bs4 import BeautifulSoup

URL = "https://tiki.vn/search?q=Apple%20AirPods%202&_lc=Vk4wMzQwMjcwMDM=&headphone_type=108271"
URL = "https://tiki.vn/chuong-trinh/dzut-co-hon"

req = requests.get(URL)
soup = BeautifulSoup(req.text, "lxml")
print(req.text)
htmlElements = soup.findAll("div", {"class": "lp-product-item sc-fjdhpX igOxad"})
print(len(htmlElements))