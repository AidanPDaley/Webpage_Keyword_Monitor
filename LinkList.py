#Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next
    
    def getData(self):
        return self.data

    def printData(self):
        print(self.data)


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
        node = Node(None)
        node.setNext(self.head)

        # delete from beginning
        if (self.head.getData() == nodeData):
            self.head = self.head.getNext()

        # delete from middle
        while (node.getNext() != None and node.getNext().getNext() != None):
            if (node.getNext().getData() == nodeData):
                node.setNext(node.getNext().getNext())
            node = node.getNext()
        # delete from the end 
        if (self.tail.getData() == nodeData):
            self.tail = node
            self.tail.setNext(None)
        

    def printList(self):
        node = self.head
        if (node == None):
            print("Empty List")
            return

        while (node != None):
            node.printData() 
            node = node.getNext()

if __name__ == "__main__":
    print("Empty List Test")
    llist = LinkList()
    llist.printList()
    

    print("Print List Test")
    for i in range(10):
        llist.addNode(Node(i))
    
    llist.printList()
    
    print("Deletion Test:")
    llist.deleteNode(6)
    llist.deleteNode(1)
    llist.deleteNode(9)
    llist.deleteNode(0)
    llist.printList()
    



