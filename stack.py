#What is a stack

#Stack is a data structure that stores items in a last-in/first-out manner (LIFO)
#udemy --> gmail --> linkedin --> website stack when using the back button in a browser

#stack using List, stack using Linked List (faster performance, but harder implementation)

class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = [] #creating a stack
    def __str__(self):
        return str(self.stack)
    def isempty(self):
        if self.list ==[]:
            return True
        else: return False
    def isfull(self):
        if len(self.list) == self.maxSize:
            return True
        else: return False
    def push(self, value):
        if self.isfull():
            return "full"
        else:
            self.list.append(value)
    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else: return None
    def peek(self):
        if len(self.stack)>0:
            return self.stack[len(self.stack)-1]
        else: return None
    

#You can also use a linkedlist for a stack, as well. 
# You would do this by constantly adding to the beginning of the linked list (push) - by pointing th head to the new node, 
# and having the reference node for the pushed node be to the last pushed node
# to pop just have the reference of head to be the current second node
#for isempty --> ifhead is None then stack is empty
# for delete --> head = None

class Node:
    def __init__(self, value = None):
        self.value=value
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head=None

class stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedLis.head == None:
            return True
        else:
            return False
    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node
    def pop(self):
        if self.isempty():
            return "invalid"
        else: 
            nodevalue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodevalue
    def peek(self):
        if self.isempty():
            return "invalid"
        else: 
            nodevalue = self.LinkedList.head.value
            return nodevalue
    def delete(self):
        self.LinkedList.head = None

