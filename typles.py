# Tuples

# create
# Access
# Edit
# Add 
# Delete
# Operations
# Functions

# Creating

T1 = () # Empty tuple
print(T1)

T2 = (1,2,3,4,5,6,7) # Homogenous Tuple
print(T2)

T3 = ("Hello",4,5.6) # Heterogenous Tuple
print(T3)

T4 = (1,2,3,(4,5)) # 2-D Tuples
print(T4)

T5 = (1)
print(type(T5))
T5 = ("Hello")
print(type(T5))
T5 = ("Hello",)
print(type(T5))

T6 = tuple("Rohtak")
print(T6)

T6 = tuple([1,2,3,4,5,6])
print(T6)

# Accessing

print(T2)

print(T2[0])

print(T2[-1])

print(T2[:4])

print(T4[-1][0])

# Editing

L = [1,2,3,4,5]

L[0] = 100
print(L)

# T2[0] = 100 # Error: 'tuple' object does not support item assignment

# Tuples just like strings are immutable.
# ADD? No

# Deleting

print(T1)

del T1 # Deleting the entire tuple
# print(T1) # Error: NameError: name 'T1' is not defined
# del T2[0] # Error: 'tuple' object doesn't support item deletion


# Operations

print(T2)
print(T3)
print(T2 + T3) # Concatenation
print(T2 * 3) # Repetition

for i in T2:
    print(i, end=" ") # Iteration
print()

print(2 in T2) # Membership

# Functions

print(len(T2)) # Length of tuple
print(max(T2)) # Maximum element in tuple
print(min(T2)) # Minimum element in tuple
print(sum(T2)) # Sum of elements in tuple
print(sorted(T2)) # Sorted tuple but it converts it into a list
print(sorted(T2),reverse = True) # Sorted tuple

# Tuples are real-only data type.
# Tuples are mainly used for data that is not going to be changed.

