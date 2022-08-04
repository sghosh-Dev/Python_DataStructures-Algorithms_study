#What is a Tuple
# a tuple is an immutable sequence of python objects, comparable and hashable

#create a tuple
newtuple = ('a','b','c','d','e')
print(newtuple)

singulartuple = ('a',) #for a singular tuple must include comma at the end or else python compiles as a string
emptytuple = tuple() #use the tuple function to clarify

newtuple1 = tuple('abcde') #use tuple function on string, and it makes a tuple with the characters of the string.
print(newtuple1)

#tuples in memory
#stores in adjacent memory location - contiguously 

#main difference for a tuple is that they are immutable - cannot be changed after being created

tupletest = ('a','b','c','d','e')

print(tupletest[-1])

#tuples also have slice operator like lists
print(tupletest[:4])

#how to traverse a tuple

#for i in tupletest:
    #print(i, end= " ")

for i in range(len(tupletest)):
    print(tupletest[i])


#How to search ffor an element in a tuple

newtuple = ('a','b','c','d','e')

print('b' in newtuple) #operation in tuple to check 

def searchtuple(Tuple, element):
    for i in Tuple:
        if i == element:
            return Tuple.index(i)
    return 'The element does not exist'

print(searchtuple(newtuple,'c'))

#Tuple operation functions
mytuple = (1,4,3,2,5)
mytuple1 = (1,2,6,9,8,7)

mytuple2 = mytuple + mytuple1
print(mytuple2)

print(mytuple * 4) #prints the sequence of the tuple to display n times

print(4 in mytuple) #checks if n is the tuple
print(mytuple.count(2)) #checks the number of times n is repeated in the tuple

print(mytuple.index(4))

print(len(mytuple))
print(max(mytuple))
print(min(mytuple))

#convert a list into a tuple
onelist = [1,2,3,4,5]
tuple(onelist)
print(onelist)

#Whats the difference between a tuple and list - a list is mutable and a tuple is immutable(cant make changes)
#You can reassign a tuple, but you cannot change a specific element in a tuple

#Tuples can be stored in lists
#lists can be stored in tuples
#both can be nested
#Tuples for hetero and lists for homo. Tuples are a little bit faster, becuase they cannot be changed