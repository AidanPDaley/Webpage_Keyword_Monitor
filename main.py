import requests
from bs4 import BeautifulSoup 

# Add Email Address to alert
def addEmailAlert(email):
    pass

# Add Website to file of monitored websites
def addWebsite(url):
    urlFile = open("urlFile.txt", "a")
    urlFile.write(str(url) + "\n")
    urlFile.close()

# get webpages from urls.txt, returns list
def getWebsiteList():
    pass

def getWebsite(url):
    webpageContent = requests.get(url)
    return webpageContent.text

# add Keyword that will be monitored on each website
def addKeyword(keyword):
   pass 

# return string of keywords read from keywords.txt
def getKeywords():
    pass

def createSoup(htmlText, htmlClass=None, htmlID=None):
    soup = BeautifulSoup(htmlText, "html.parser")
    # later add way to change the class value
    # maybe create a new function that creates the soup
    # so that this is only for searching the soup
    if (htmlClass):
        soup = soup.find_all(class_=htmlClass)
    if (htmlID):
        soup = soup.find_all(id=htmlID)
    return soup
# searches to see if keywords are present in specified tag and returns
# list of the contents of that tag if keyword is present
def searchKeywords(soup, keywords):
    for child in soup:
        for keyword in keywords:
            if (keyword in str(child.string)):
                print(str(child.string))


if __name__ == "__main__":
    addWebsite("https://bjjfanatics.com/collections/daily-deals?page=1")
    addWebsite("https://bjjfanatics.com/collections/daily-deals?page=2")
    addWebsite("https://bjjfanatics.com/collections/daily-deals?page=3")

    websiteContent = getWebsite("https://bjjfanatics.com/collections/daily-deals?page=1")

    soup = createSoup(websiteContent,htmlClass="product-card__name")
    searchKeywords(soup, ["Bodoni", "Mica", "Danaher", "Meregali", "Jones", "Ryan"])






