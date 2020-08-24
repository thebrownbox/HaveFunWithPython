import requests
from bs4 import BeautifulSoup

URL = "https://tiki.vn/search?q=Apple%20AirPods%202&_lc=Vk4wMzQwMjcwMDM=&headphone_type=108271"
 
req = requests.get(URL)

soup = BeautifulSoup(req.text, "lxml")
items = soup.findAll("a", {"class": "search-a-product-item"})
#body > div.wrap > div > div.product-listing > div:nth-child(2) > div.product-box-list > div:nth-child(2)
print(len(items))

for item in items:

    #https://tiki.vn
    url = "https://tiki.vn" + item.get("href")

    # print(item.get("title"))
    price = item.find("span", {"class":"final-price"}).get_text()


    # <span class="price-regular">6.900.000đ</span>
    regularPrice = item.find("span", {"class":"price-regular"}).get_text()

    finalPrice = str(price).split("đ")
    print(finalPrice[0].strip() + " (" +finalPrice[1].strip()+")" + " | " + regularPrice)



    print(url)


# print(items[0])