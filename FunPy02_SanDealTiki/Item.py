class Item:
    def __init__(self, name = "N/A", url = "None"):
        self.name = name
        self.url = url

    def info(self):
        print("Name: " + self.name + "\n" + "Url: " + self.url)
