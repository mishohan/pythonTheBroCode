# 2D - Collection: List; as it's flexible
# 2D list = [list-1, list-2, list-3]

fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [["apple", "orange", "banana", "coconut"], ["celery", "carrots", "potatoes"], ["chicken", "fish", "turkey"]]
# groceries = [fruits, vegetables, meats]


# fruits[0]
# print(fruits)

print(groceries[0][0]) # apple
print(groceries[0][1])
print(groceries[0][2])
print(groceries[0][3])
print(groceries[1][0])


# itterate over with nested list
for collection in groceries:
    # print(collection)
    for food in collection:
        print(food, end=" ")
    print()

