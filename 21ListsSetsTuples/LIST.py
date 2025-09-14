# collection = single "variable" used to store multiple values
# List = [] ordered and changeable, Duplicates OK
# set = {} unordered and immutable, but Add/Remove OK. NO duplicates
# Tuple = () ordered and unchangeable. Duplicates OK. FASTER


# LIST = [] ordered and changeable, Duplicates OK
fruits = ["Apple", "Orange", "Banana", "Coconut"]

print(fruits)
print(fruits[0])
print(fruits[1])
print(fruits[2])
# print(fruits[4]) # error
print(fruits[0:3])
print(fruits[:3])
print(fruits[::2])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)

#different methods in list
# print(dir(fruits))
# print(help(fruits))

#length of a list
print(len(fruits))

# determine weather a value is in the list: in operator
print("Apple" in fruits) # returns boolean

# lists are changeable
fruits[0] = "pineapple"
print(fruits)

#append
fruits.append("strawberry")
print(fruits)

#remove method
fruits.remove("strawberry")
print(fruits)

# insert method
fruits.insert(0, "apple")
print(fruits)

# sort method
fruits.sort()
print(fruits)

# reverse method
fruits.reverse()
print(fruits)

# clear method
# fruits.clear()
# print(fruits) # []

# index of an element
print(fruits.index("Coconut"))

# counting how many of the same element on the list
print(fruits.count("Orange"))