
# LISTS AND ARRAYS ARE POWERFUL TOOLS TO STORE COLLECTION OF DATA IN PYTHON 

list_1 = [1,2,3,4]

print(list_1) # printing the list normally

print(list_1[1]) # printing the members of the list using indexing

print(type(list_1)) # printing the type of the data type

list_2 = [1,"a",2,3.14,"mayank",True] # python has given us the freedom to put any type of data in one single list to work with and it will work normally

print(list_2)


# WHEN WE ARE DEALING WITH LARGE DATA SETS WE WILL BE USING ARRAYS INSTEAD OF LISTS

## NEW INFO WE GOT THAT LISTS ARE MUTABLE NOT LIKE STRINGS

list_3 = [1,2,3,4,6]

print(list_3[4])

list_3[4] = 5

print(list_3)

print(len(list_3)) #using len function to the find and print the length of any list

## THERE'S A NEW FUNCTION KNOWN AS sum() which only works for numeric data types list's which like gives you the total sum of all the members of a numeric list.

list_4 = [20,54,321,3219,39321.7]

print(sum(list_4))

#| Q - We have a dataset of the marks of the students and the teacher has to find the mean score from the values of all the students

marks = [87, 76, 95, 68, 80, 83, 92, 74, 79, 89]

mean_marks = sum(marks)/len(marks)

print("The mean marks for all of the students are: " + str(mean_marks))