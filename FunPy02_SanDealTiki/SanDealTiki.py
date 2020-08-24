INPUT_FILE = "items.txt"

inputFile = open(INPUT_FILE, "r")
itemList = inputFile.readlines()
inputFile.close()

# Show the content file
# for s in itemList:
#     print(s)