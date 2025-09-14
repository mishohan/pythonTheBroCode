# collection = single "variable" used to store multiple values
# List = [] ordered and changeable, Duplicates OK
# set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# TUPLE = () ordered and unchangeable. Duplicates OK. FASTER
fruits = ("apple", "orange", "coconut", "banana", "coconut")
print(fruits)

#different methods in tuple
# print(dir(fruits))

# for indepth discription of these attributes and methods
# print(help(fruits))

# #length of a set
print(len(fruits))

# determine weather a value is in the tuple: in operator
print("apple" in fruits) # returns boolean

# index of elements
print(fruits.index("banana"))

# count
print(fruits.count("coconut"))

# itterable
for fruit in fruits:
    print(fruit)