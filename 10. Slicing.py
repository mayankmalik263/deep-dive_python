
#| Slicing 

# sequence [start:stop:step]

# start : the index from the slicing begins (inclusive).
# stop : the index at which the slicing ends (exclusive).
# step : the number of elements to skip between each included element.

my_string = "Hello World"

print(my_string[0:5]) #Output = Hello
print(my_string[4:12]) #Output = o World

print(my_string[::2]) 
#@ OUTPUT CONCEPT

## 1st = H
## 2nd = H + 2 = H e "l" == l 
## 3rd = l + 2 this means that there are 2 steps of addition 1st will be l then second will be the second l in hello then it will print o 
## And the cycle continues....

#: IMPORTANT (REVERSING A STRING)

print(my_string[::-1])

## The same will be applied for all the data types.

string1 = "strategy"
 
# Output should be "yget"

print(string1[-1:-5:-1])

'''
When i didn't wrote the last -1 on the step index the string was print as a blank space

That's correct! When you don't specify the step index, it defaults to 1. So, if you wrote print(string1[-1:-5]), 
it would try to slice the string from the last character (index -1) to the 5th character from the end (index -5), 
but since the step is 1, it would try to move backwards, which is not possible. 
As a result, it would return an empty string.
'''

