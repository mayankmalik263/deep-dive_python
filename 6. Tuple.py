
#| TUPLES ARE ALSO THE SAME AS STRINGS BUT THE MAJOR DIFFERENCE IS THAT TUPLES ARE IMMUTABLE

tuple_1 = (1,2,"abc",4,3.5)
print(tuple_1)
print(type(tuple_1))

## AN INTERESTING THING ABOUT A TUPLE IS THAT IF YOU WANT ONE ELEMENT YOU CAN GET THAT BY JUST ADDING A COMMA AFTER ONE ELEMENT

tuple_2 = (2,)
print(tuple_2)
print(type(tuple_2))

#|if we do this with the comma this will return as a int data type not a tuple

#@ IMMUTABILITY

tuple3 = (1,2,3)
#-tuple3[0] = "change"
#:THIS CODE WILL GIVE A TYPE ERROR
'''    
tuple3[0] = 0
    ~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
'''
print(tuple3)

## BUT THERE'S STILL A WAY TO CHANGE THE ELEMENT OF A TUPLE BY CONVERTING IT INTO A LIST AND THEN AGAIN TO TUPLE

tuple4 = list(tuple3) #Storing the tuple as a list in a separate variable
tuple4[0] = "change" #Changing the value of the element
tuple3 = tuple(tuple4) #change the list back to the tuple
print(tuple3) #printing the tuple which is converted from a string


