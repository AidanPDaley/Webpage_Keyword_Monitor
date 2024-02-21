# Class to hold information about what the user wants to monitor
class WebMonitor:
    def __init__(self, url=None, htmlClass=None, htmlID=None, email=None, keywords=[]):
        self.url = url
        self.htmlClass = htmlClass
        self.htmlID = htmlID
        self.email = email
        self.keywords = []

    # Getter Methods
    def getUrl(self):
        return self.url

    def getHtmlClass(self):
        return self.htmlClass
    
    def getHtmlID(self):
        return self.getHtmlID(self)

    def getEmail(self):
        return self.email
    
    def getKeywords(self):
        return self.keywords
    
    # Setters
    def setUrl(self, url):
        self.url = url

    def setHtmlClass(self, htmlClass):
        self.htmlClass = htmlClass

    def setHtmlID(self, htmlID):
        self.htmlId = htmlID

    def setEmail(self, email):
        self.email = email

    def setKeywords(self, keywords):
        self.keywords = keywords
    
    # keyword list handlers
    def addKeyword(self, keyword):
        self.keywords.append(keyword)

    def deleteKeyword(self, keyword):
        self.keywords = [w for w in self.keywords if w != keyword]


    def __str__(self):
        print(f"{self.url}, {self.htmlClass}, {self.htmlID}, {self.email}, {self.keywords}")

if __name__ == "__main__":
    test = WebMonitor()
    test.__str__()

    test2 = WebMonitor("test.com", "class_", "id", "aidan.p.daley@gmail.com", ["Bodoni", "Danaher", "Ryan"])
    test2.__str__()

    test3 = WebMonitor(url="test.com",htmlClass="class_", keywords=["Bodoni", "Danaher", "Ryan"])
    test3.__str__()


