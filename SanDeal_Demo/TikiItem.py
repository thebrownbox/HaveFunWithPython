
class TikiItem:
    def __init__(self):
        self.title = ""
        self.price = 0
        self.regularPrice = 0
        self.url = ""
    
    def info(self):
        return self.title +" | " + str(self.price) + " | " + self.url

    def isValidItem(self, patterns):
        for p in patterns:
            if self.title.lower().find(p.lower()) < 0:
                return False
        return True