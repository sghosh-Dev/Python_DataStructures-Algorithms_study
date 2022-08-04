#An array is only for homogenous data types
#An array is contigious, there are no spaces between them, in memory
#Each element has its unique index
#The size of an array cannot be changed (If full you cannot add another one, without deleting one)
#Instead of declaring 500 integers, declare one array with size 500

#Types of Array
#array's can be one dimensional or multi-dimensional
#one dimensional: an array with a bunch of values being declared with a single index - Access using a[i]
#two dimensional: an array with values being declared with double index - A[i][j] (RowxCol)
#three dimensional: Multiple 2 dimensional, values being declared with double index A[i][j][k]

#Stored in RAM
#stored contiguously, in one row. But labeled with their index - for 1,2,...N dimensional array

#Creating an array
#Assign it to a variable, define the type and the size to reserve space in RAM
#Python doesnt have a built in Array D struct, have to import array library
from array import *
from itertools import count
arr1 = array('i', [1,2,3,4,5,6])#integer
arr2 = array('d',[1.1,1.2,1.3,1.4])
print(arr1)
print(arr2)

#insertion into array, if any spaces available. Specifiy the index and set it equal to the data
print()
arr3 = array('i',[1,2,3,4,5,6])
arr3.insert(6,7)
print(arr3)

#if you insert an element to an existing index, it pushes the existing elements down one index (i +1)
arr3.insert(0,0)
print(arr3)
arr3.insert(3,5)
print(arr3)

print()
#Traverse an Array

def traversearray(array):
    count =0
    for i in array:
        if i%2 == 0 and len(array) != 0:
            count += 1
    return count
            
print()
print(arr3)
print(traversearray(arr3))

#Access array element
first = arr3[3]
print(first)

def accesselement(array, index):
    if len(array)<=index:
        print("Error, invalid index")
    else:
        print(array[index])

accesselement(arr3,2)

def findelement(array, n):
    count = 0
    for i in array:
        if i == n:
            count +=1
    print(count)

print()
print(arr3)
findelement(arr3, 5)

def findelement1(array,n):
    for i in array:
        if i==n:
            return arr3.index(n)
    return "This value does not exist"

print()
print(arr3)
print(findelement1(arr3,1))

#Deletion
#When deleting an array, not at the end, all elements to the right will move one to the left

print()
arr4 = array("i",[1,2,3,4,5,6])
print(arr4)
arr4.remove(3) #removes the first occurance of 3, not the element at index 3
print(arr4)

#A two dimensional array, is an array with a bunch of values having been declared with double index
#Two Dimensional arrays are just multiple 1d arrays stacked on top of each other.
#a[i]j[j]

import numpy as np #need for 2d arrays

tda = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(tda)

#insertion to tda - cannot insert a single value, must insert a row or column

#Adding column, when added all columns to the right of the insertion will move one to right 
#Adding row, when added row all row underneath will move one space down
print()
#tda1 = np.insert(tda, 0, [[1,2,3,4]], axis=0) 
#which array to insert into new one, which index to put it, 1d array to inset, and which axis (0-row or 1-col)
#print(tda1)

#can use append instead of insert of inserting into the last index
tda1 = np.append(tda,[[1,2,3,4]], axis=0)
print(tda1)

#Access an element of two dimensional Array
#print(tda1[0][0])
print(len(tda))

def accesselement(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex>= len(array[0]):
        print('This is not valid')
    else: print(array[rowIndex][colIndex])


accesselement(tda1, 3, 2)

#Traversing two Dimensional Array, traverses by row - goes through each column from 0 to n starting at the 0th row
def traversetda(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end =' ')

print(tda1)
print()
traversetda(tda1)

def searchtda(array, n):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == n:
                return 'the value is located at index' +str(i) +' '+str(j)
    return 'cannot find'

print()

print(searchtda(tda1, 14))

print()
print()
#Deletion - Two Dimensional array
#Deleting Col - Because you cant have an empty column, columns to the right have to move one to left each
#Deleting row - Because you cant have an empty row, rows below have to move one row up.
#Delete Col or row using NP.

twoDimarray = np.array([[11,15,10,6],[10,14,11,5],[12,17,12,8],[15,18,14,9]])
print(twoDimarray)
print()
newtwoDimarray= np.delete(twoDimarray,0, axis=1) #original array, index number, row or col (1 is col)
print(newtwoDimarray)
print()
twoDimarray = np.delete(twoDimarray,1, axis=1) 
print(twoDimarray)

from array import *

#1. Create an array and traverse
arr1 = array('i',[1,2,3,4,5,6,7])

for i in arr1:
    print(i)

#Access individual elements through indices 
print('Question 2')
print(arr1[0])

#Append any value to the array using append() method
print('Question 3')
arr1.append(9)
print(arr1)

#Insert value in an array using insert() method
print('Question 4')
arr1.insert(0,7) #number index to be placed, "X" - moves elements to the right one
print(arr1)

#Extend python array using extend() method
print('Question 5')
arr2 = array('i',[10,11,12])
arr1.extend(arr2) #Adds second array2 to array1. Arr1 = arr1+arr2
print(arr1)

#Add items from list into array using fromlist() method
print('Question 6')

list1 = [13,14,15]
arr1.fromlist(list1)
print(arr1)

#Remove any array element using remove() method
print('Question 7')
arr1.remove(2) #removes the first instance of n, and moves all elements to the left
print(arr1)

#Remove last array element using pop() method
print('Question 8')
arr1.pop()
print(arr1)

#Fetch any element through its index using index() method
print('Question 9') #prints the value at that indec
print(arr1.index(7))

#Reverse a python array
print('Question 10')
arr1.reverse()
print(arr1)

#Check for number of occurrences of an element using count()
print('Question 11')
arr1.append(5)
print(arr1)
print(arr1.count(5))

print('Question 12')
#convert array to string using tostring() method
#strtemp = arr1.tostring()
#print(strtemp)

#Convert array to a python list with same elements using tolist() method
print('Question 13')
#print(arr1.tolist())

#slice elements from an array
print('Question 14')
print(arr1)
print(arr1[0:5]) #slices index X:Y

