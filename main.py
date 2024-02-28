import requests
from bs4 import BeautifulSoup 
from webMonitor import WebMonitor 

# get webpages from urls.txt, returns list
def getWebsiteList():
    pass


if __name__ == "__main__":
    keywords = ["Garcia", "Bodoni", "Mica", "Danaher", "Meregali", "Jones", "Ryan"]
    
    wb = WebMonitor(url="https://bjjfanatics.com/collections/daily-deals?page=1", \
                        htmlClass="product-card__name", keywords=keywords) 
    wb.createSoup()
    wb.searchKeywords() 






