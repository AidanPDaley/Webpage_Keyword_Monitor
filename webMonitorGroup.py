from webMonitor import WebMonitor
from LinkList import *  

class WebMonitorGroup:
    def __init__(self, webMonitorFile):
        self.webMonitorFile = webMonitorFile
        self.group = LinkList() 
    
    # reads from webMonitorFile and stores webmonitors in the group property
    def createWebMonitors(self):
        file = open(self.webMonitorFile, "r")
        
        lines = file.readlines()
        for line in lines:
            if (line): 
                wm = self.parseLineToWebMonitor(line)            
                self.addWebMonitor(wm)

        file.close() 
 
    # takes line from file, returns web monitor object 
    def parseLineToWebMonitor(self, line):

        line = [l.strip() for l in line.split(",")]
        wm = WebMonitor(name=line[0], \
                        url=line[1], \
                        htmlClass=line[2], \
                        htmlID=line[3], \
                        email=line[4], \
                        keywords=line[5::])
        return wm

    # writes new webmonitor data to file
    def addWebMonitor(self, wm):
        node = Node(name=wm.getName(), data=wm)
        self.group.addNode(node) 
    
    # deletes webMonitor by name
    def deleteWebMonitor(self, name):
        self.group.deleteNodeByName(name)
    
    
    def runWebMonitors(self):
        node = self.group.getHead()
        while (node):
            wm = node.getData()
            wm.createSoup()
            wm.searchKeywords()
            wm.printResult()
            node = node.getNext()

    # lists the names of the webMonitors
    def listWebMonitors(self):
        print("Web Monitors: ")
        self.group.printList()
    

if __name__ == "__main__":
    wmg = WebMonitorGroup("./urlFile.txt")
    wmg.createWebMonitors()
    print("First Group:==============}") 
    wmg.listWebMonitors() 
    wmg.deleteWebMonitor("bjj5")
    print("Post Deletion:============") 
    wmg.listWebMonitors() 
