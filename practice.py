# "how are you?" -> "How Are You?" without using the title function

sample = "how are you?"

split = sample.split(" ")
print(split)

final = []

for i in split:
    print(i.capitalize(), end = " ")
    final.append(i.capitalize())

print(final)
print(" ".join(final))

# My score for this question -> 6/10

# abc@gmail.com -> we want 'abc' from the email id

email = "abc@gmail.com"

split_1 = email.split("@")
# print(split_1)

first_part = split_1[0]
print(first_part)

# My score for this question -> 7/10

# [1,1,2,2,3,3,4,4] -> [1,2,3,4]

L = [4,1,1,2,2,3,3,4,4]
l = list(set(L))
print(l)

# My score for this solution to this question -> 3/10
l = []
## Real solution

for i in L:
    if i not in l:
        l.append(i)
l.sort()
print(l)