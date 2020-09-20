from TikiTarget import TikiTarget

def getTargetsFromFile(fileName):
    targetFile = open(fileName, "r")
    lines = targetFile.readlines()
    targetFile.close()

    targets = []
    n = len(lines)
    print("n = " + str(n))
    i = 0
    while i < n:
        newTarget = TikiTarget(lines[i].strip(), lines[i+1].strip())
        # print(newTarget.info())
        targets.append(newTarget)
        i = i+2

    return targets

# 1.499.000đ => 1499000
def convertToPrice(strPrice):
    strPrice = strPrice.replace('.', '')
    strPrice = strPrice.replace('đ', '')
    return int(strPrice)