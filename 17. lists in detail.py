'''
what are lists?
list vs array
create
access
edit
add
delete
operations
functions
'''

# array v list
# 1. arrays -> homogenous lists -> heterogenous
# 2. arrays mein continuously cheeze stored hoti h where as list mein different places pe stored hoti h cheeze
# 3. arrays are much faster
# 4. lists are more programmer friendly but slow


# creation

l = []
# OR
l = list()

l = [1,2,3]

l2 = ["Hello",2,5.6,True,5+6j]

# multi-dim lists
# 2D
l3 = [1,2,[3,4]]

# 3D
l4 = [[[1,2],[3,4]],[[5,6],[7,8]]]

l5 = list("Mayank")

# accessing

l[0]

l[-1]

l[1:3]

l[::-1]

print(l3)

l3[0] # but i want to access the '4' in the list inside of this list

l3[-1]

x=l3[-1]

x[0]

l3[-1][0]

print(l4[1][1][0])

# editing

l
l[0]=100
l[-1]=500

l[1:4]=[200,300,400]
l

# adding

# append
# extend
# insert

l.append(1000)
l.append("Hello")

l.extend([5000,6000,7000]) # this will be appended as individual elements

l.append([5,6]) # and this will be appended as a single whole list element

l.extend("goa") # so each character of goa will be appended as single elements or you can say it always appends multiple elements

l.insert(1,"World") # this will insert world at the 1st index and it will be INSERTED! remember that
print(l)

# Delete

# del
# remove
# pop
# clear

print(l2)
del l2
# print(l2) #: this will through an error that 'l2' is not present

del l[0] # deleting elements according to their indexing value

del l[-4] # can also access through -ve indexing

del l[-3:] # this will remove the whole goa portion from the list

# remove is used when you don't know the index position of the element you want to delete
print(l)
l.remove("Hello")
print(l)

# pop is used to delete the last element of the list

l.pop()
print(l)

# clear will not delete your list like delete but will make it empty but the list will stay there defined

l.clear()
print(l)


# OPERATIONS

# concatenation
L = [1,2,3,4]
L1 = [5,6,6,8]

print(L + L1)

# multiplication

print(L * 3)

# loops

for i in L:
    print(i)

print(l3)
for i in l3:
    print(i) # 1 2 [3,4]

# membership operations

print(4 in l3)
print(4 in l3[-1])
print([3,4] in l3)

# FUNCTIONS

print(len(L))

print(min(L))
print(max(L))
print(sorted(L))
print(sorted(L,reverse=True)) # this is not a permanent in the main list the main list 'L' still remain the same not reversed

sort = L.sort() # this is a permanent operation
print(sort)

index = L.index(3) # this will print the index of the number you put in it
print(index)