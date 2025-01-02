# strings => these in python particularly, a sequence of Unicode Characters

#@ Creating strings

c = 'Hello'
print(c)
c = "Hello" # always use the ("") 
print(c)
c = str("Hello")
print(c)

# For more refer to (4. Data types, string.py)

#@ Accessing a substring from a string

# Concept of Indexing
print(c[0]) # accessing the character at the 0th index of the string that is stored in c

# if we try to give the indexing out of the range of the string it will show an out of range error

# +Ve indexing (0 to n-1 (where n is the length of the string)) (L TO R)
# -Ve Indexing (-n to -1) (like if you type -1 then it will access the last character of the string) (R TO L)
print(c[-1])

#@ Slicing

c = "Hello World"
print(c[0:5]) # (as we already know that the starting will be inclusive and ending will be exclusive and with that will get the output "Hello")
# SYNTAX => c[start:end:step]

print(c[2:]) # this means that i want everything from 2 onwards

print(c[:4]) # this means that i want everything till 4-1=3 

print(c[:]) # well this gives you the whole string

print(c[2:6:2]) # will start from 2nd => l then go to 4 as the step is 2 => o and then as 6 is exclusive we can't got any further so it will end 
print(c[0:8:3])

print(c[0:6:-1]) # this output i guess is : dlroW | Okay so this wrong because when you are working with +ve string so step can't be -ve

print(c[-1:-6:-2]) # this will work but the above one gives you empty string

print(c[-5:-1:2]) # but this will work because well we are actually moving forward

print(c[::-1]) # this is the best use case for me personally because this is simplest one line code for reversing a string

# Using -1 as the step in string slicing reverses the direction of traversal, but the indices must be properly set to achieve the desired result. 
# For full string reversal, [::-1] is the simplest approach.

print(c[-1:-5:-1])

#@ EDITING AND DELETING STRINGS

c = "Hello"
print(c)
# c[0] = 'X' this will be an error because strings are immutable
# but yes you can reassign in python 
c = "World"
print(c)
# yes you can also not add any new characters to a string using the indexing method

# Deletion

del c
# print(c) this gives the error that c is not defined because we have deleted 'c' 

c = "World"
# del c[0] gives you the error => 'str' object doesn't support item deletion like you cannot delete a particular character from any string

# del c[:3:2] this will also give the same error as we try to delete a portion from the string it will mutate the string ofc and that is not possible.

#@ String Operations

# 1. Arithmetic -> +(concatenation) and *

print("Hello"+"-"+"World")

print("$"*50)

# 2. Relational

print("Hello" == "World")
print("Hello" != "World")
print("Mumbai">"Pune")# here the result will be based lexiographically like the word that comes first in the dictionary will be the smaller one
print("Goa"<"Kolkata")
print("Rohtak">"rohtak")# This will be false because the small letters comes later in the dictionary atleast after the capital ones so the smaller letters are greater than bigger ones

# 3. Logical

# "" -> False
# "feaddwa" -> True

print("Hello" and "World") # T1 and T2 -> T2
print("" and "World")# F and T -> F
print("" and "")# F and F -> f

print("" or "World") # F or T -> T
print("hello" or "world") # T1 or T2 -> T1

print(not "Hello")
print(not "")

# 4. Loops

for i in "Rohtak":
    print(i)
print("============================")
a = "Hello World"
for i in a[2:7:2]:
    print(i)

# 5. Membership 
c = "Mayank"
print("M" in c)
print("m" in c)
print("M" not in c)
print("m" not in c)

#@ String Functions

# Common functions(common for all iterables)
# 1. len
# 2. max
# 3. min
# 4. sorted

b = "Haryana"
print(len(c))

print(max(b)) # gives you the biggest character in the string according to the ASCII Values

print(min(b)) # similar to max() just returns the minimum ASCII value character

print(sorted(b)) # sorts the characters of any string in ascending order on the basis of their ASCII Values in form of a list

#  to get the result in descending order

print(sorted(b,reverse=True))

# Now comes the only functions unique to strings

# 1. Capitalize/Title/Upper/Lower/Swapcase

print(b.capitalize()) # it just capitalize the 1st character of the string but doesn't change the real string 
print("i'm happy".capitalize())

print(b.title())
print("i'm happy".title()) 
# changes every starting character of the word to capital

print(b.upper()) # everything will be in upper case
print(b.lower()) # everything will be in lower case

print("HeLlO wORld".swapcase()) # this will change the upper -> lower and lower -> upper

# 2. count 

print("it is raining".count("i"))

# 3. Find/Index

print("it is raining".find("g"))

print("it is raining".find("x")) # this will give -1 as the character is not in the given string

print("it is raining".index("rain"))

# print("it is raining".index("x")) # this will give you a substring not found error

# 4. endswith/startswith

print("it is raining".endswith("ing"))

print("it is raining".startswith("it"))

# 5. format

print("Hello my name is {} and I am {}".format("Mayank",18))
# can be used in a login page where you don't know that what will be the user's name so you use format string function there

print("Hello my name is {1} and I am {0}".format("Mayank",18))
# the 0 and 1 are the index values of the values given in the format function

print("Hello my name is {name} and I am {age}".format(name = "Mayank",age = 18))
# 3rd variation

print("Hello my name is {age} and I am {weight}".format(name = "Mayank", age = 18, weight = '70kg'))
# it is not important that agr yahan pe h toh use hi karoge and we can also like age in both the curly braces

# 6. isalnum/isalpha/isdecimal/isdigit/isidentifier

print("flat20".isalnum()) # checking for alphanumeric

print("flat20&".isalnum()) # false because & is a special character

print("flat".isalpha()) # for alphabets only

print("45".isdigit())

print("Hello world".isidentifier())
print("Hello_world".isidentifier())

# 7. split

print("who is the pm of india".split())
# quora uses this to creates tags of every single word

print("who is pm of india".split("pm"))
# can also split on a particular word
print("who is pm of india".split("i"))

print("who is pm of india".split("x"))
# here there will be no split in the string and the whole string will be stored as one

# 8. join (just the reverse of split function)

print(" ".join(['who','is','the','pm','of','india']))
print("-".join(['who','is','the','pm','of','india']))

# 9. Replace

print("Hi my name is Manmeet".replace("Manmeet","Mayank"))

# 10. Strip

name = "              Mayank              "
print("Hi "+name)
x = name.strip()
print("Hi "+x)