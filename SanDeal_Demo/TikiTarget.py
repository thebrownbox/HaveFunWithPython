
class TikiTarget:
    def __init__(self, patternStr="", categoryStr = ""):
        self.patternsString = patternStr
        self.patterns = self.__splitPattern()
        self.categoryUrl = categoryStr
    
    def info(sefl):
        return "Patterns: " + str(sefl.patterns) + " | category: " + sefl.categoryUrl

    def __splitPattern(sefl):
        newList = sefl.patternsString.split(",")
        i = 0
        while i < len(newList):
            newList[i] = newList[i].strip()
            i = i+1
        return newList

    # Máy ảnh, lấy liền, Fujifilm =>  Máy ảnh lấy liền Fujifilm
    def getKeyword(sefl):
        keyword = ""
        for key in sefl.patterns:
            keyword = keyword + " " + key
        return keyword
    
    def getSearchLink(sefl, pageNum):
        return sefl.categoryUrl +"?q="+ sefl.getKeyword() + "&ref=categorySearch&page=" + str(pageNum)