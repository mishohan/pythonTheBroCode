# collection = single "variable" used to store multiple values
# List = [] ordered and changeable, Duplicates OK
# set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# SET = {}

fruits = {"apple", "orange", "coconut", "banana"}

print(fruits)

#different methods in set
# print(dir(fruits))

# for indepth discription
# print(help(fruits))

# #length of a set
print(len(fruits))

# determine weather a value is in the list: in operator
print("apple" in fruits) # returns boolean

# set object is not subscriptable
# print(fruits[0]) # throws an error

# add method
fruits.add("pineapple")
print(fruits)

# remove method
fruits.remove("pineapple")
print(fruits)

# pop method
print(fruits.pop())

# clear
print(fruits.clear())