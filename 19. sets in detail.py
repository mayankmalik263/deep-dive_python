# sets

# it do not allow duplicates
# sets have no indexing/slicing
# sets dont allow mutable data types
# set itself is a mutable data type

#@ Creating

S1 = {}
print(type(S1)) # this will be a dictionary 
#  to create an empty set we can do this

S1 = set()
print(type(S1))

S1 = {1,2,3,4,5}
print(S1)
S2 = {"Hello",4.5,True}
print(S2)
S3 = {1,1,2,2,3,3}
print(S3)

#: S4 = {[1,2,3],"Hello"} this will through an error as list is a mutable data type

S4 = {(1,2,3),"Hello"} # using tuple as it is an immutable data type
print(S4) 

# sets have no indexing 
# sets have hashing which will explain why hello comes first here

#: S5 = {{1},{2}} this will an error as sets in sets are not allowed because sets are unhashable data tyoe

#@ Access

# print(S1[0]) Through an error of 'set' object does not support  which includes positive indexing, negative indexing and slicing also

#@ Editing

# Which is also no possible in sets

# and if you are thinking of using like list here converting the set into list and then again into the same set variable it will always have a different memory address

print(S1)
print(id(S1))
L = list(S1)
print(L)
L[0] = 100
print(L)
S1 = set(L)
print(S1)
print(id(S1))

#@ Adding

print(S1)
S1.add(6)
print(S1)
print(id(S1))
S1.add(7)
print(id(S1))

#@ Deleting

print(S2)
del S2
# print(S2) throughs an error that S2is not defined

# del S1[0] this will not work as you know 

S1.remove(100)
print(S1)

S1.pop() # will pop out the very last element of the set which according to hashing is 2
print(S1)

#@ Set operations

S1 = {1,2,3,4,5}
S2 = {3,4,5,6,7}

# S1 + S2 Which is not possible

# S1 * 3 which is also not possible

for i in S1:
    print(i)

print(1 in S1)

#@ Functions

print(len(S1))

print(min(S1))

print(max(S1))

print(sum(S1))

print(sorted(S1)) # this will convert the set into a list

print(sorted(S1, reverse = True))

#@ Functions unique to SETS

print(S1.union(S2))

print(S1.intersection(S2))

print(S1.difference(S2)) # the items which are in S1 not in S2

print(S2.difference(S1)) # the items which are in S2 not in S1

print(S1.symmetric_difference(S2)) # items which are not in common in both the sets

print(S1.isdisjoint(S2)) # False as they have some elements in common

print(S1.issubset(S2)) # False all the items of S2 are not in S1

print(S1.issuperset(S2)) # False

print(S1.clear()) # None because now S1 is an empty set






