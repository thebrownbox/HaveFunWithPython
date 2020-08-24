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
        item = Item(lines[i].strip(), lines[i+1].strip())
        listItem.append(item)
        i += 2

    return listItem
