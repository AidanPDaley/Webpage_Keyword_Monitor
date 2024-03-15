from webMonitor import WebMonitor
from LinkList import *  

class WebMonitorGroup:
    def __init__(self, webMonitorFile):
        self.webMonitorFile = webMonitorFile
        # look at different data structure (Doubly linked list?) 
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

        line = line.strip().split(", ")
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
        #print(f"Name: {node.getName()}, Data: {node.getData()}")
        self.group.addNode(node) 
    
    # deletes webMonitor by name (add webmonitor name to WebMonitor Class)
    def deleteWebMonitor(self, name):
        pass
    
    # lists the names of the webMonitors
    def listWebMonitors(self):
        self.group.printList()


if __name__ == "__main__":
    wmg = WebMonitorGroup("./urlFile.txt")
    wmg.createWebMonitors()
    wmg.listWebMonitors() 
