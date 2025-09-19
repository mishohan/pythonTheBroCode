# dictonary = a collection of {key:value} pairs
#             ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# For all the attributes and method of a dictonary
# print(dir(capitals))
# For indepth discription
# print(help(capitals))

# print(capitals.get("USA"))
# print(capitals.get("India"))
# print(capitals.get("Japan")) # None

# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")

capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# print(capitals.get("USA"))

capitals.pop("China") # Removes china key pair

capitals.popitem()   #Removes the newly added key value pair 

# capitals.clear() # Clear the dictonary

# To get only the keys
Keys = capitals.keys()
print(Keys)

for key in capitals.keys():
    print(key)

# To get only the values
values = capitals.values()

for value in capitals.values():
    print(value)

# Items method
items = capitals.items()
print(items)

for key, value in capitals.items():
    print(f"{key}: {value}")