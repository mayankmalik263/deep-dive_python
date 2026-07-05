# Dictionaries
#@ Creating 
D = {"Name":"Mayank","Gender":"Male"}
print(D)

# R1: Dictionary has no indexing
# R2: Dictionary is a mutable types
# R3: Key -> Immutable, Values -> They can be mutable
# R4: Keys should be unique

# Mutable -> List/Sets/Dictionary
# Immutable -> String/Tuples/Int/Float/Boolean/Complex

#: D1 = {[1,2,3]:"Hello"} This will through an error of unhashable type 'list'

D1 = {(1,2,3):"Hello"} # using tuple instead of list
print(D1)

D2 = {"Name":"Rahul","Name":"Rohit"}
print(D2)

D3 = {"Name":"Rohit","College":"HIT","Marks":{"M1":56,"DS":54,"Eng":67}} #2-d dic
print(D3)

#@ Accessing

# D[0] won't work as indexing is not present in Dictionaries

print(D["Name"])
print(D["Gender"])
print(D)
print(D3)
print(D3['Marks'])
print(D3['Marks']['DS'])

#@ Editing

D['Name']='Rahul'
print(D)

D3['Marks']['DS'] = 64
print(D3)

#@ Function to get the value of any key in the dictionary

x = D.get('Name')
print(x)
# but this function can't be used for 2-D Dictionaries

#@ Adding new key-value pairs

D['Age']=18
print(D)

D3['Marks']['DE']=43
print(D3)

#@ Deleting
D5 = {}
print(D5)
del D5

del D['Age']
print(D)

D.clear() # makes 'D' an empty dictionary

#@ Operations

# Concatenation & multiplication doesn't work

for i in D3:
    print(i)

for i in D3:
    print(i,':',D3[i])

# membership operators

print('Rohit' in D3)
print('Name' in D3)
# membership operators only works on keys not like on the values that the key stores

print(len(D3))
print(min(D3)) # according to the ASCII VALUE
print(max(D3)) # according to the ASCII VALUE

print(sorted(D3))
print(sorted(D3,reverse=True))

print(D3.keys()) # gives the list of the all the keys in the dictionaries

print(D3.values()) # gives the list of the all the values in the dictionary



