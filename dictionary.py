#What is dictionary?
#A dictionary is a collection which is unordered,changeable, and indexed
#dictioanries have key-value pairs, retrieve data using a key

#in a list/array the index positions have to be integers but in a dictionary tehy can be any type

mydict = dict()
seconddict = {}

engtosp = {"one":"uno", "two":"dos","three":"tres"}
print(engtosp)
print(engtosp["three"])

#how are dictionaries represented in memory?
# dict are indexed by keys and are associated arrays
#dicts are implemented using hash tables - an array whose indexes are obtianed using a hash function
# A hash table is a way of doing key-value lookups. You store the values in an array, and then use a hash function to find the index of the array cell
# that corresponds to your key-value pair  
print()
#update/add am element to the dictionary

mydict = {'name':'Edy','age':26}
#change a value
mydict['age'] = 27
print(mydict)

#add a value
mydict['address'] = 'London'
print(mydict)

print()
#Traverse through a dictionary
def traversedict(dict):
    for key in dict:
        print(key, dict[key])

traversedict(mydict)

print()
#Search for an element in a dictionary - linear search
def searchdict(dict,value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return "not found"

print(searchdict(mydict, 27))

#how to delete or remove an element from a dictionary
mydict.pop('name')
print(mydict)

#popitem() - remove and return and arbitrary number
#mydict.popitem() #this would remove something randomly

#clear() removes everything from the dictionary
#mydict.clear()

del mydict['age']
print(mydict)
del mydict #deletes everything