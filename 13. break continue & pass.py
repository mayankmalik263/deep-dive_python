# Break

for i in range(1,11):
    if i == 9:
        break
    print(i)
# normally break is used in linear searching like finding a user name "Rahul" which is at the 100th place in the database of 100000 then will you go the 100000
# if you have found Rahul on the 100th place ofc not thats where the break statement comes into play.

# CONTINUE
print("------------------------")
for i in range(1,11):
    if i == 5 :
        continue
    print(i)
    print("Hello")

# normally continue statement can be used when you don't want to print something but still want to iterate over the whole loop
# for e.g -> if i want to show all the names of the items that in stock and want to skip the items which are out of stock then you should continue statement

# PASS

for i in range(1,11):
    pass
# now due to the pass statement there will no error in this code and this code will just be like passed nothing will be done of it