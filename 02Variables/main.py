#  Variable = A container for a value(string, integer, float, boolean)
#             A variable behaves as if it was the value it contains


# STRINGs
first_name = 'Shohan' 
food = "Pizza"
email = "shohan@gmail.com"

print(first_name) # Shohan
#f-string convention: - for writting varable name along some text
print(f"Hello, {first_name}.") # Hello, Shohan.
print(f"You like {food}.") # You like Pizza.
print(f"Your email is {email}") # Your email is shohan@gmail.com


# INTEGERs
age = 25
quantity = 3
num_of_students = 30

print(f"You're {age} years old.") # You're 25 years old.
print(f"You're buying {quantity} items.") # You're buying 3 items.
print(f"Your class has {num_of_students} students.") # Your class has 30 students


# FLOARs
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your GPA is: {gpa}")
print(f"You ran {distance}km")


# BOOLEANs
is_student = True # or False
print(f"Are you a student? : {is_student}")
if is_student:
    print("You're a student")
else: 
    print("You're NOT a student.")

for_sale = True # or False
if for_sale:
    print(f"That item is for sale")
else:
    print(f"That item is NOT available")

is_online = False
if is_online:
    print("You're Online")
else:
    print("You're Offline")