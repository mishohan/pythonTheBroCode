# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >=100:
    print("You're too old to sign")
elif age >= 18:
    print("You're now signed up")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be 18+ to sing up")

#Another Example

response = input("Would you like food? (Y/N)")

if response == "Y":
    print("Have some food!")
else:
    print("No food for you!")

#Another Example

name = input("Enter your name: ")

if name == "":
    print("You didn't type in your name")
else:
    print(f"Hello {name}")

# Last Example

for_sale = True # or False

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")

online = False

if online:
    print("You're Online!")
else:
    print("You are Offline!")