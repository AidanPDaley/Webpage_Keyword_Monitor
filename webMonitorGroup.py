import queue
from webMonitor import WebMonitor

class WebMonitorGroup:
    def __init__(self, webMonitorFile):
        self.webMonitorFile = webMonitorFile
        # look at different data structure (Doubly linked list?) 
        self.wmQueue = queue.Queue(maxsize=0)
    
    # reads from webMonitorFile, creates the webMonitors, and adds them to the queue
    def createWebMonitors(self):
       pass  
 
    # takes line from file, returns web monitor object 
    def parseLineToWebMonitor(self, line):
        pass
    
    # writes new webmonitor data to file
    def addWebMonitor(self, wm):
        pass
    
    # deletes webMonitor by name (add webmonitor name to WebMonitor Class)
    def deleteWebMonitor(self, name):
        pass
    
    # lists the names of the webMonitors
    def listNames(self):
        pass


if __name__ == "__main__":
    wmg = WebMonitorGroup()
