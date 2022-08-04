#What is a linked list
#sequential collection, made up of independent nodes of any data type with a reference to the next node doesnt have to be in order
#Each node has data and a link to the next node, the link of the tail is 'null'
#To get to the end of linked list, you haev to traverse through each node
#a linked list is not contiguous in memory but rather pointers to memory location using the reference at the end of a linked list

#Linked Lists vs Arrays
# Elements of a linked lists are independent objects (even if you delete one node, the list still works). In an array, you cannot delete a cell.
# Variable size, the size of linked list is not predefined
# Insertion and removeals in a linked lsit are very efficient, whereas an array is better for searching as each element is indexed

#Types of Linked List
#Singly Linked List - Each node has data, and a reference to the next node - no referenceto the previous node. The head and tail do not have any data, only reference to the first/last node
#Circular singly linked list - same as singly linked list, except the last node (not the tail), also holds a reference to the first node
#   Benefit of a CSLL is that it gives the option to return to the first node, after traversing to the last node, whereas the last node of a SLL is null
#Doubly Linked List - Each node has data, and two references, the node before and after it. Otherwise similar to linked list
#   Can traverse backwards as well
#Circular doubly linked list - Same as doubly linked list, except the last node has a next_node reference to the first node.

#The first node is assigned head node and the last node is assigned the tail node

#Linked List in memory are not stored contiguously, but instead are stored in various locations with pointers sequentially.

#Creating a singly linked list
#Create head and tail, initialize with null -> create a blank node and assign a value to it and reference to null ->Link head and tail with there node
from platform import node

class Node:
    def __init__(self, value = None):
        self.value=value
        self.next = None

class slinkedlist:

    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self): #to print the sll
        while node:
            yield node
            node=node.next
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head =newNode
            self.tail =newNode
        else:
            if location == 0:#Inserting an element to the beginning
                newNode.next=self.head
                self.head = newNode
            elif location == 1:#Inserting an element to the end
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else: #Inserting an element to the middle
                tempNode = tempNode.next
                index =0
                while index < location -1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    #Singly Linked List Traversal
    # --> start --> Check head, Yes? --> Loop, No? -->Terminate
    def traversesll(self):
        if self.head is None:
            print("Invalid")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    #Search for a node in a SLL
    def searchSLL(self, nodeValue):
        if self.head is None:
            return "Invalid"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "Invalid"
    #Delete a node from singly linked list
    def delsll(self, location):
        if self.head is None:
            print("invalid")
        else:
            if location ==0: #from beginning, only one node
                if self.head == self.tail:
                    self.head=None
                    self.tail=None
                else: #more than one node
                    self.head = self.head.next
            elif location ==1:
                if self.head == self.tail:
                    self.head=None
                    self.tail=None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node






singlylinkedlist = slinkedlist() #Creates a linkedlist init with a head and tail (empty)
node1 = Node(1) #assigns nodes
node2 = Node(2)

singlylinkedlist.head=node1
singlylinkedlist.head.next = node2
singlylinkedlist.tail = node2