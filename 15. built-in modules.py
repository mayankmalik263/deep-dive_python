# print(help('modules')) # to get the list of all the modules available on your system

import math
import random
import time
import os

print(math.pi)
print(math.e)
print(math.factorial(6))
print(math.ceil(6.5))
print(math.floor(6.5))
print(math.sqrt(9))
print("=======================================================")
print(random.randint(1,100))
a = [1,2,3,4,31,45,123]
random.shuffle(a) # this variable permanently shuffles any iterable you give to it
print(a)
print("=======================================================")
print(time.time()) # this gives you the timestamps means ki the total number of seconds from midnight of 1 jan 1970 till the current date
print(time.ctime())
print("Hello")
print(time.sleep(1)) # this will gives you the lag/delay of 1 sec in the next code to give the output
print("World")
print("=======================================================")
print(os.getcwd())
print(os.listdir())