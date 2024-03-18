from webMonitor import WebMonitor 
from webMonitorGroup import WebMonitorGroup

if __name__ == "__main__":
    wmg = WebMonitorGroup("./urlFile.txt")
    wmg.createWebMonitors()
    wmg.listWebMonitors()
    wmg.runWebMonitors()


