#Lists in python are built in
#A list is a data structure that holds an ordered collection of items, examples below

integers=[1,2,3,4]
print(integers)
stringlist=['Milk', 'cheese', 'Butter']
print(stringlist)
mixed_list = ['spam', 1.2,5]
print(mixed_list)
nested= ['spam',2.0,5,[10,20]]
print(nested)
empty=[]
print(empty)

#Accessing/Traversing the list
shoppinglist=['Milk', 'cheese', 'Butter']
print(shoppinglist[1])
for i in shoppinglist:
    print(i, end=' ')
#if you try accessing an element not in the range of the list, you will get an error

print('Milk' in shoppinglist) #use this notation to check if an element exists in a list (will return true if in the list)

#You can use negative numbers to access elements in the list as well, up to - (len). from index 0, -1 is the last element in the list
print()
for i in range(len(shoppinglist)):
    shoppinglist[i] = shoppinglist[i] + "+"
    print(shoppinglist[i]) #if in for loop prints each on a separate line

print(shoppinglist) #prints everything on one line

#You cannot traverse through an empty list

#how to update and insert elements in a list

list1=[1,2,3,4,5,6,7]
print(list1)
#The order of elements will be the same elements as we decalred them until we change them
print()
list1[2] = 33
print(list1)
#list1[100] = 2 returns an error
#time comp to access an element is O(1)

#Insert an element to the beginning, any given place, end, or append another list
print()
mylist=[1,2,3,4,5,6,7]
print(mylist)
mylist.insert(0,11) #index of insertion and element to be inserted
print(mylist)
print()

mylist.append(10) #adds an element to the end of a list
print(mylist)

mylist2 = [11,12,13,14]
mylist.extend(mylist2)

print(mylist)

#How to delete an element from a list
letlist = ['a','b','c','d','e','f']

#slicing operations
print(letlist[:2]) # from the beginning to 2
print(letlist[2:]) #from 2 to the end of the list

letlist[:2] = ['x','y'] 
print(letlist)

#deleting elemetns from a list
letlist2 = ['a','b','c','d','e','f']
print(letlist2.pop(1))#deletes the element at the index inside the pop function
print(letlist2)

del letlist2[1:3]
print(letlist2)

#the remove element is useful when you know the element that you know you want to remove
letlist2.remove('f')
print(letlist2)

#Searching for an element in the list
#In operator
intlist = [10,20,30,40,50,60,70,80,90]

if 20 in intlist:
    print(intlist.index(20))
else: print('not here')

#Linear search
def searchinlist(list, n):
    for i in list:
        if i == n:
            return list.index(n)
    return 'This value does not exist'
print()
print(searchinlist(intlist,20))

print()
#List operations and functions
a=[1,2,3]
b=[4,5,6]
c= a+b
print(c)

d=[0,1]
d=d*4
print(d)

z=[]
for i in range(11):
    z.append(i)

print(z)

print(len(z))
print(max(z))
print(min(z))
print(sum(z))

mylist=[]

#while(True):
 #   inp = input('Enter a number: ')
  #  if inp == 'done': break
   # value = float(inp)
    #mylist.append(value)

#average = sum(mylist)//len(mylist)
#print(average)


#Strings and Lists

a ='spam'
b= list(a)
print(b)

m = 'spam-spam-spam'
delimiter ='-' #what separates each word in the initial string, if a space, than delimeter is not required
n = m.split(delimiter) #converts string to list
print(n)

#list to string
print(delimiter.join(n)) #converts list to string

#drawbacks of lists
somelist = [2,4,7,2,4,1,3]
somelist1 = sorted(somelist)
somelist.sort()
print(somelist1)

print(somelist)


#Lists versus arrays
#Both ds are mutable (can be changed)
#both can be indexed and iterated through
#They can be both sliced
#array for arithmetic operations
#List can have multiple different types of data, array will be converted to a string








