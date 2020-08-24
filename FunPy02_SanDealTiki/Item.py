class Item:
    def __init_(self, name="", price=0, url=""):
        self.name = name
        self.price = price
        self.url = url
        self.discount = ""
        self.regularPrice = ""

    def printInfo(self):
        print(self.name + ": " + self.price + "(" + self.discount + ") " + self.regularPrice)