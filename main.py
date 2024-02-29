from webMonitor import WebMonitor 

if __name__ == "__main__":
    keywords = ["Garcia", "Bodoni", "Mica", "Danaher", "Meregali", "Jones", "Ryan"]
    
    wb = WebMonitor(url="https://bjjfanatics.com/collections/daily-deals?page=1", \
                        htmlClass="product-card__name", keywords=keywords) 
    wb.createSoup()
    result = wb.searchKeywords() 
    print(result)

