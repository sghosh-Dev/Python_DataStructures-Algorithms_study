#What is hashing
#Hashing is a method of sorting and indexing data. - allow large amount of data to be indexed using keys commonly created by formulas

#Hashing is time efficient in case of search operations

#hash function: a function that can be used to map data of arbitrary size to data of fixed sized
#key: Input data
#Hash Value: value return by hash function
#hash Table: data structure which implements an array, a structure that can map keys to values
#Collision: A colliosion occurs when two different keys, map to the same hash value using the HF

#a common hash function is modulo --> the key % len(hash)
def mod(x, length):
    return x % length

#a common hash function for string is using ASCII
def modASCII(string, length):
    total=0
    for i in string:
        total += ord(i)
    return total % length

#Collision Resolution Techniques
#direct chaining: impleemnts the buckets as linked list. Colliding elements are stored in this lists

#Open addressing sols:
#linear Probing: Places new key into closes following empty cell
#Quadratic Probing: adding arbitrary quadratic polynommial to teh index until an empty cell is found 1^2, 2^2, 3^2. 
#  --- if the hash cell is taken, add the index by 1^2 (a[i+1]), if thats taken as well then add that by 2^2 (a[i+1+4]), keep doing this until a space is open

#double hashing
#  --- a second HF is given, if the hash val is taking add HF2 to HF1. Keep doing that until an open space is found.


#What to do if a hash table is full
#wont happen in direct chaining (linked list)
#Open addressing: Create 2x size of current hash table and recall hashing for current keys

#if the input size is known --> use open addressing
#Use direct chaining when deletion is popular