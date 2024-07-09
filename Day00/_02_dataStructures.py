# string
# Stings are immutable which means everytime we perform a operation on the string new string is returned by the inbuilt functions and the string remains unchanged
# string = "helLo"
# print(string.upper())
# print(string.lower())
# print(string)
# print(string.capitalize())

# print(string.count("l"))
# print(string[0:3])
# print(string[1:4])

# List
# lists are mutable
# list = [1,2,3,4,5]
# # print(list[-2])
# list.pop()
# # print(list)
# list.append(2)
# print(list)

# list.remove(2)
# print(list)

# list.sort()
# print(list)
# list[0] = 10
# print(list)

# list2 = [41, 42, 43, 44, 45, 46, 47]
# list.extend(list2)
# print(list)
# list.sort()
# print(list)

# print(list[0:4])

# dictionaries
# dictionary is a mutable object which works on key value pair

dict1 = {}
# print(type(dict1))
# dict2 = {"key": "value", "key2": "value2"}
# print(dict2["key"])

# dict3 = {"one": "ek", "two": "don", "three": "teen","teen":"anuradha"}

# print(dict3["teen"])

# print(dict3.keys())
# print(dict3.values())
# print(dict3.items())

dict1 = {"key1": 1, "key2": 2, "key3": 3, "key4": 4, "key5": 5, "key6": 6}
for a in dict1.keys():
    print(a) 
