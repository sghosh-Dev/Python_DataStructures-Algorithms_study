class HF:

    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)] #Creates an array of size 100 elements, with each element being None

    def get_hash(self,key): #key value pair, gets a key and gets teh ASCII value of each character and adds them up, takes that mod 100 to get the cell index
        h=0
        for char in key:
            h += ord(char)
        return h %self.max 

    def add(self,key,value): #add the value into the cell that you get from hashing the key
        h= self.get_hash(key)
        self.arr[h] = value

    def get(self, key):
        h= self.get_hash(key)
        return self.arr[h]


t = HF()
t.add('march 6', 130)

print(t.get('march 6'))

class HF1:

    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)] #Creates an array of size 100 elements, with each element being None

    def get_hash(self,key): #key value pair, gets a key and gets teh ASCII value of each character and adds them up, takes that mod 100 to get the cell index
        h=0
        for char in key:
            h += ord(char)
        return h %self.max 

    def __setitem__(self,key,value): #add the value into the cell that you get from hashing the key
        h= self.get_hash(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h= self.get_hash(key)
        return self.arr[h]

        #with the changes, you can just do t[key, value] to add an item into the array (__setitem__)
        #and t[key] to get the value from the array

#dealing with collisions by Linkedlists

class HT:

    def __init__(self):
        self.max = 100
        self.arr = [[] for i in range(self.max)] #Creates an array of size 100 elements, empty

    def get_hash(self,key): #key value pair, gets a key and gets teh ASCII value of each character and adds them up, takes that mod 100 to get the cell index
        h=0
        for char in key:
            h += ord(char)
        return h %self.max 

    def __setitem__(self,key,value): #add the value into the cell that you get from hashing the key
        h= self.get_hash(key)
        #Prior used to overwrite the value
        #Update an existing value: check if that value exists and update it if so
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0]==key: #element 0 being the key part of the key-value part
                self.arr[h][idx] = (key, value)
                found=True
                break
            if not found:
                self.arr[h].append((key, value)) #if the key doesnt exist add it to the linkedlist

    def __getitem__(self, key):
        h= self.get_hash(key)
        return self.arr[h]