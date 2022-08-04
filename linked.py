class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None
    def listprint(self): #traversing and printing the list
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    def AtBeginning(self, newdata):
        newNode = Node(newdata) #sets nextval and dataval to none
    
        newNode.nextval = self.headval #sets the pointer of the new head node to the old head node
        self.headval = newNode #sets the head node attr to the new node
    def AtEnd(self, newdata):
        newNode = Node(newdata)
        if self.headval is None:
            self.headval = newNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = newNode
    def Inbetween(self,middle_node,newdata):
      if middle_node is None:
         print("The mentioned node is absent")
         return

      NewNode = Node(newdata)
      NewNode.nextval = middle_node.nextval
      middle_node.nextval = NewNode

    def removenode(self, removekey):
        HeadVal = self.head

        if(HeadVal is not None):
            if(HeadVal.data == removekey):
                self.head = HeadVal.next
                HeadVal = None
                return
        while(HeadVal is not None):
            if HeadVal.data == removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        
        if(HeadVal == None):
            return
        prev.next = HeadVal.next
        HeadVal = None


#Creating a SLinkedList
list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

#Link the first node to the second node
list1.headval.nextval = e2
#Link the second node to the third node
e2.nextval = e3

#list1.listprint() #to print

list1.AtBeginning("Sun")
#list1.listprint()
list1.AtEnd("Thu")
#list1.listprint()

list1.Inbetween(list1.headval.nextval, "Fri")
list1.listprint()