
#| Dictionaries are powerful tools in python which allows you to store key value pairs which are really helpful in working with complex data structures

marvel = {"Name":"Thor",
          "Place":"Asgard",
          "Nickname":"God of Thunder",
          "Weapon":"Hammer",
          1:2,
          3 : "Level",
          "Power":"Lightning",
          "allies":["iron man", "captain america"],
          "abc":{1:2,
                 3:4}
          }
print(marvel["abc"]) #calling the values by their key
print(marvel)
print(type(marvel))
print(marvel[3])
print(type(marvel[3]))
print(marvel["allies"][0]) #using the indexing to call the first string from the 2 that have been stored in the key "allies"
#print(marvel[4]) #:THIS WILL GIVE A KEY ERROR

customer = {
    "Name":"Mayank",
    "id": 12345,
    "email":"mayankxyz@gmail.com"
}

customer["email"] = "mayank@gmail.com" #updating email address
customer["phone"] = 55555 #adding a new key and value
del customer["id"] #deleting a key and the value

print(customer)

print(marvel.keys()) #this will print the keys as normal like dict_keys
print(list(marvel.keys())) #this will print the keys in the form of a list

## THE SAME CAN GO FOR THE VALUES [.values()]

print(list(marvel.values()))

## IF YOU WANT ALL THE ITEMS OF THE DICTIONARIES [.items()]

print(list(marvel.items()))

#| Q - John has this data which is trying to sort like very inefficiently try to make it efficient :
#| ["Mango","Mango","Pineapple","Pineapple","Apple","Mango","Banana","Banana","Pineapple","Apple","Pineapple"]
fruits = ["Mango","Mango","Pineapple","Pineapple","Apple","Mango","Banana","Banana","Pineapple","Apple","Pineapple"]
fruits_sorted = {}

fruits_sorted["Mango"] = fruits.count("Mango")
fruits_sorted["Apple"] = fruits.count("Apple")
fruits_sorted["Pineapple"] = fruits.count("Pineapple")

print(fruits_sorted)





