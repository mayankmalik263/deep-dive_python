# when to use nested loops
# it is totally based on the experience 
# but like nested loops are not a very good solution to a question because their time complexity is n^2

# real life scenario cases of nested loops
# like to check the transactions made by the users of the bank so like one loop will iterate over the number of people in the bank
# and the second will iterate over the number of transactions made by each user of the bank

'''
*
**
***
****
*****
'''

# logic of the question can like we have 2 loops here ne is for the rows and the other is for the columns

# for i in range(1):
#     for j in range(1,6):
#         print(j*"*")

# for i in range(1,6):
#     print(i*"*")

rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))

for i in range(1, rows+1):
    for j in range(0, i):
        print("*", end=" ")
    print("")
    
#: Bonus tip: go to pythontutor.com to visualize this code and show that how it works

