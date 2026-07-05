# problem 1
list_1 = [1,2,3,4,5,6,7,8,9,10]

sum = 0
for i in list_1:
    sum += i
print(sum)

max = list_1[0]
for i in list_1:
    if(max < i):
        max = i
print(max)

# max_2 = sorted(list_1)[-1]
# print(max_2)

min = list_1[0]
for i in list_1:
    if(min > i):
        min = i
print(min)

# min_2 = sorted(list_1)[0]
# print(min_2)

# problem 2

list_2 = [10, 20, 30, 40, 50]

list_2.remove(30)
print(list_2)
list_2.insert(2,35)
print(list_2)

# problem 3

cities = ("Rohtak","Dehradun","Mumbai")

# cities[0] = "Bhiwani"

# ERROR
#     cities[0] = "Bhiwani"
#     ~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# problem 4

frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "Java", "JavaScript"}

print(frontend & backend)
print(backend - frontend)
# print(frontend + backend)

tech_stack = frontend.union(backend)
print(tech_stack)

# Mini Project

students = [
  ("Mayank", 89, "CSE"),
  ("Kanusha", 91, "AIML"),
  ("Rohit", 76, "ECE")
]



