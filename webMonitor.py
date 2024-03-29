# Class to hold information about what the user wants to monitor
import requests
from bs4 import BeautifulSoup

class WebMonitor:
    def __init__(self, name="None", url="None", htmlClass="None", htmlID="None", email="None", keywords=[]):
        self.name = name 
        self.url = url
        self.htmlClass = htmlClass
        self.htmlID = htmlID
        self.email = email
        self.keywords = keywords 
        self.soup = None
        self.result = ""

    # Soup
    def createSoup(self):
        self.soup = BeautifulSoup(self.getHtmlText(), "html.parser")
        if (self.htmlClass != "None"):
            self.soup = self.soup.find_all(class_=self.htmlClass)
        if (self.htmlID != "None"):
            self.soup = self.soup.find_all(id=self.htmlID)
    
    def searchKeywords(self):
        for child in self.soup:
            for keyword in self.keywords:
                if (keyword in str(child.string)):
                    self.result += str(child.string)
        if self.result == "":
            self.result = "No Matches\n"

    def getSoup(self):
        return self.soup

    # Getter Methods
    def getName(self):
        return self.name

    def getUrl(self):
        return self.url

    def getHtmlText(self):
        r = requests.get(self.url)
        return r.text

    def getHtmlClass(self):
        return self.htmlClass
    
    def getHtmlID(self):
        return self.htmlID

    def getEmail(self):
        return self.email
    
    def getKeywords(self):
        return self.keywords

    def getResult(self):
        return self.result
    
    # Setters
    def setName(self, name):
        self.name = name

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
   
    def printResult(self):
        print(f"{self.name} Result: \n{self.result}")

    def __str__(self):
        print(f"{self.name}, {self.url}, {self.htmlClass}, \
        {self.htmlID}, {self.email}, {self.keywords}")

if __name__ == "__main__":
    test = WebMonitor()
    test.__str__()

    test2 = WebMonitor("test.com", "class_", "id", "aidan.p.daley@gmail.com", ["Bodoni", "Danaher", "Ryan"])
    test2.__str__()

    test3 = WebMonitor(url="test.com",htmlClass="class_", keywords=["Bodoni", "Danaher", "Ryan"])
    test3.__str__()


