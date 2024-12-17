
#| SETS ARE THE COLLECTION OF UNIQUE ELEMENTS I.E. A UNORDERED COLLECTION OF UNIQUE ELEMENTS
'''
    1. SETS CAN NOT HAVE DUPLICATES IN IT
    2. SETS ARE MUTABLE LIKE STRINGS
    3. YOU CAN MAKE A NON-EMPTY SET WITH CURLY BRACES BY SPECIFYING EACH ELEMENTS USING COMMA
'''  

empty_set = set()
print(type(empty_set))

nonempty_set = {5,4.56,1,"abc",1} #As this set has one duplicate value "1" when we print the set it will only print one of them
print(nonempty_set) # as printing the set it will delete all the duplicates

nonempty_set = nonempty_set | {"mayank",65,-9}
print(nonempty_set)

## WE CAN USE len() function here to find the length of the set

print(len(nonempty_set))

empty_set2 = {} #THIS IS A DICT NOT A SET
print(type(empty_set2))

## IF YOU ALL THE UNIQUE ELEMENTS IN A LIST YOU CAN CAST IT TO A SET AND THEN PRINT THE ELEMENTS

list_1 = [1,2,1,2,3,4,4,3,4,5,6,5,5,5,6]
set_1 = set(list_1)
print(set_1)

#: IMPORTANT - WE CANNOT STORE MUTABLE ITEMS IN A SET BECAUSE IT IS IMMUTABLE

# my_set = {1,2,[3,4]} as you see here we have 3 and 4 as a list which is wrong we will get a type error in it as there is a unhashable type 'list' in there.

#: BUT WE CAN ADD TUPLES BECAUSE THEY ARE ALSO IMMUTABLE
my_set = {1,2,(3,4)}
print(my_set)

## WE CAN ALSO NOT ADD SETS INTO A SET!!!!!!!