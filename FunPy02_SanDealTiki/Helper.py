from Item import Item

def getItems(fileName):
    inputFile = open(fileName, "r")
    lines = inputFile.readlines()
    inputFile.close()
    
    lineCount = len(lines)
    listItem = []

    i = 0
    while i < lineCount:
        # print(lines[i])
        if(len(lines) == 0):
            break
        item = Item(lines[i], lines[i+1])
        listItem.append(item)
        i += 2

    return listItem
