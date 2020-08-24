class Item:
    def __init__(self):
        print("Create new object!")

    def sayHello():
        print("Hello world!")

    def sayHello2(self):
        print("Hello world! 2")

    def sayHi(self):
        print("Hi!")

    def __del__(self):
        print("Desconstructor!")

Item.sayHello()
Item.sayHi()