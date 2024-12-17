# Data types are use to categorize the data that a variable or object can hold.
# Python has several data types :
#     1. Numbers
#     2. Strings
#     3. lists
#     4. tuples
#     5. dictionaries


#@ ---------------------- STRINGS ----------------------------

first_String = "Hello World"

print(first_String)

phrase = "Hello My name is Mayank Malik"

print(phrase) 

print(type(phrase))

#: TIP : ALWAYS USE THE DOUBLE QUOTES INSTEAD OF SINGLE ONES.

#line = 'I'm fine # - SO YOU MIGHT NOT FACE THIS ERROR (Remove this statement from comment you will see the error)
line = 'I\'m fine' # - You can also use back slash
line = "I'm fine"
line_2 = '''
This is a 
MultiLine
String
'''

print(line)
print(line_2)


#@ ---------------- IMMUTABILITY -----------------------------

message = "Hey muddy, How are you?"
# So there's a typo that i want to write buddy but i wrote muddy
# So will just do this
print(message[4]) # "4" is used for indexing 
message.replace("muddy","buddy") #With the use of replace the string should have replaced with
print(message)

#As you can see that even after using the replace function we can not even change the string which the data type = string is immutable 

#- But we want to change the string so we can like declare the replace function in another variable but there will be another way of doing this in the further lectures

message_2 = message.replace("muddy","buddy")
print(message_2)

#- As we can see that the string is now changed

#@ ---------------------- SOME BASIC OPERATIONS -----------------------------

algo = "Neural Networks"
len(algo)

#- len function is used to get the length of the string

print(len(algo))

#- to print the length of the string

algo.count("Ne")
print(algo.count("Ne"))

#- This count functions returns the count of the string in the longer string and this function will take the smaller string which you want the of as ARGUMENT.

#@ ------------------------ CHALLENGE -------------------------------
#: 1.
books = "Python Book 1, Python crash course, Learn Python the hard way, Starting out with Python, Automate Boring stuff with python, Python for Everyone"

e_counts = books.count("e")

print("The number of 'E/e' in the following string is " + str(e_counts))
#- You are wondering why we use str here? so here's the reason like if we try to go without the e_counts are undefined because all the values to print are a string and e_counts is an integer value
#: print("The number of 'e' in the following string is " + e_counts)
''' Traceback (most recent call last):
  File "e:\Personal Practice\Python\Data types, strings.py", line 80, in <module>
    print("The number of 'e' in the following string is " + e_counts)
          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~
#: TypeError: can only concatenate str (not "int") to str
'''
#- There will be type error i have explained earlier

#@ Now 1 thing to note that this program has read all the e's like on the small ones but i want to read all the "E/e" so this program will convert all the string to lower case and then count the number of e-s so that all get counted in it.

small_e = books.lower().count("e")

print("The number of 'e' in the following string is " + str(small_e))

#: 2.

#FIND A ERROR IN THIS CODE

num_str = "25"
#result = num_str + 5 #TYPE ERROR IS THERE IT CAN FIXED WITH A QUICK CONVERSION
result = int(num_str) + 5
print(result)

