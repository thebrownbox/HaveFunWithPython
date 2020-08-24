class Target:
    def __init__(self, name = "N/A", maxPrice = 1000, url = "None"):
        self.name = name
        self.url = url
        self.maxPrice = maxPrice

    def info(self):
        print("Name: " + self.name + "\n" + "PRICE: " + self.maxPrice + "\n" + "Url: " + self.url + "\n")
