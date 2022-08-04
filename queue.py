#Creating a Queue with collections library
from collections import deque
customQ = deque(maxlen=3) #create a Queue
customQ.append(1) #enqueue
customQ.popleft() #dequeue
customQ.clear()

#Creting a FIFO Queue with the queue
import queue as q
#Methods of this library, qsize(), empty(), full(), put(), get(), task_done(), join()
customqu = q.queue(maxsize =3)
customqu.qsize()
customqu.put(1) #appends


#What is a queue? A Que is a data structure that stores items in FIFO
#Enqueue/Dequeue insertion/removal

#creating a Queue is just initializing an empty list

#Creating a Queue without setting a size limit
#Queue using a list
class queue:
    def __init__(self):
        self.items = []
    def __str__(self): #printing
        values = [str(x) for x in self.items]
        return " ".join(values)

    def isempty(self):
        if self.items ==[]:
            return True
        else:
            return False
    
    def enqueue(self, value):
        self.items.append(value)
    
    def dequeue(self):
        if self.isempty():
            return 'invalid'
        else:
            return self.items.pop(0) #pop usually deletes the last element, but pop(0) deletes the first
    
    def peek(self):
        if self.isempty():
            return 'invalid'
        else: return self.items[0]

    def delete(self):
        self.items = None

customQueue = queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
customQueue.dequeue()
print(customQueue)
print(customQueue.peek())

#Queue using a LinkedList
#This is just removing the link from the head to the first node and instead to the second. and adding between the last element and the tail

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head =None
        self.tail = None
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode=curNode.next

class Queue:
    def __init__(self):
        self.linkdlist = LinkedList()
    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return ' '.join(values)   
    def enqueue(self, value):
        newNode = Node(value)
        #if no node is present, link head and tail to the new tail
        if self.linkedlist.head ==None:
            self.linkedlist.head = newNode
            self.linkedlist.tail = newNode
        #if other nodes present, then add the new node to the end of the linked list
        else:
            self.linkedlist.tail.next = newNode
            self.linkedlist.tail = newNode
    def isempty(self):
        if self.linkedlist.head == None:
            return True
        else: return False
    def dequeue(self):
        if self.isempty(): return " "
        #to dequeue is to disconnect the link between the head and the first element and connect it to the second element, as then mem garbage collection takes it away
        tempNode = self.linkedlist.head
        #check if there any other nodes other than ehad and list
        if self.linkedlist.head == self.linkedlist.tail:
            self.linkedlist.head = None
            self.linkedlist.tail = None
        else: #creating a link between the second node and head
            self.linkedlist.head = self.linkedlist.head.next
        return tempNode
    def peek(self):
        if self.isempty():
            return " "
        else: return self.linkedlist.head
    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None

#Time and space complexity for a queue is O(1), except when enqueue/dequeue in a list and creating a queue with a caplist

#Circular Queue
class capqueue:
    def __init__(self, maxsize = 10): #create queue with fixed size
        self.items = maxsize *[None]
        self.maxsize = maxsize
        self.items = []
        self.start = -1
        self.top = -1
    def __str__(self): #printing
        values = [str(x) for x in self.items]
        return " ".join(values)
    def isfull(self):
        if self.top +1 == self.start:
            return True
        elif self.start ==0 and self.top + 1 == self.maxsize: #inital when no dequeue needed to happen to enqueue
            return True
        else: 
            return False
    def isempty(self):
        if self.top == -1:
            return True
        else: return False
    def enqueue(self, value):
        if self.isfull():
            return 'full'
        else:
            if self.top +1 ==self.maxsize: #top is pointing to the last cell, have to point it back to the beginning
                self.top=0
            else:
                self.top +=1 #if top is not at the end, then go to the next cell
                if self.start == -1:
                    self.start=0
            self.items[self.top]=value
    def dequeue(self):
        if self.isfull():
            return 'full'
        else:
            firstelement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start =-1
                self.top =-1
            elif self.start +1 ==self.maxsize:
                self.start +=1
            self.items[start] = None
            return firstelement










