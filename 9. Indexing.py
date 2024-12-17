
#| INDEXING LEFT TO RIGHT - 0 TO n-1
#| INDEXING RIGHT TO LEFT - n-1 TO 0

my_string = "Hello, World!"

print(my_string[0]) #- H
print(my_string[-1]) #- !

my_tuple = (1,23,4,5,6)
print(my_tuple[1]) #- 23

my_list = [1,2,3,4,5,6,7]
print(my_list[-3])#- 5

my_dict = {"a": "A",
           2: "B",
           "c": "C",
           4: "D",
           "e": "E",
           6: "F"
           }
print(my_dict["a"]) # dictionaries are indexed using the keys
#: QUES - 
marvel = ["iron man","X-men","Spider-Man","Captain America","Deadpool","Wolverine","Dr. Strange","Namor"]

marvel_1 = [marvel[0],marvel[2],marvel[4],marvel[6]] #team odd
marvel_2 = [marvel[1],marvel[3],marvel[5],marvel[7]] #team even

print(marvel_1,marvel_2)



