# import Item as it
from Item import Item

INPUT_FILE = "items_25.txt"

inputFile = open(INPUT_FILE, "r")
itemList = inputFile.readlines()
inputFile.close()

it.Item()
Item()