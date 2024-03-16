#Linked List

class Node:
    def __init__(self, name, data):
        self.name = name
        self.data = data
        self.next = None

    def getName(self):
        return self.name

    def getNext(self):
        return self.next

    def setName(self, name):
        return self.name

    def setNext(self, next):
        self.next = next
    
    def getData(self):
        return self.data

    def printData(self):
        print(self.data)
    
    def __str__(self):
        print(f"Name: {self.name}, Data: {self.data}, --> ")

class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
   
    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail


    def addNode(self, node):
        if (self.head == None):
            self.head = node
            self.tail = node
        else:
            self.tail.setNext(node)
            self.tail = node
        
    def deleteNode(self, nodeData):
        node = Node(None, None)
        node.setNext(self.head)

        # delete from beginning
        if (self.head.getData() == nodeData):
            self.head = self.head.getNext()

        # delete from middle
        while (node.getNext() != None and node.getNext().getNext() != None):
            if (node.getNext().getData() == nodeData):
                node.setNext(node.getNext().getNext())
            else:
                node = node.getNext()
        # delete from the end 
        if (self.tail.getData() == nodeData):
            self.tail = node
            self.tail.setNext(None)
        
    def deleteNodeByName(self, nodeName):
        node = Node(None, None)
        node.setNext(self.head)

        # delete from beginning
        if (self.head.getName() == nodeName):
            self.head = self.head.getNext()
        # delete from middle
        while (node.getNext() != None and node.getNext().getNext() != None):
            if (node.getNext().getName() == nodeName):
                node.setNext(node.getNext().getNext())
            else:
                node = node.getNext() # delete from the end 
        if (self.tail.getName() == nodeName):
            self.tail = node
            self.tail.setNext(None)

    def printList(self):
        node = self.head
        if (node == None):
            print("Empty List")
            return 
        while (node != None):
            print(node.getData().__str__())
            node = node.getNext()

if __name__ == "__main__":
    print("Empty List Test")
    llist = LinkList()
    llist.printList()
    

    print("Print List Test")
    for i in range(10):
        llist.addNode(Node(f"Name{i}", i))
        llist.addNode(Node(f"Name{i}", i))
    llist.printList()


    print("Deletion Test:")
    llist.deleteNode(6)
    llist.deleteNode(1)
    llist.deleteNode(9)
    llist.deleteNode(0)
    llist.deleteNodeByName("Name2")
    llist.printList()
    




