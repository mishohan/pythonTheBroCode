# while loop = executes some ocde WHILE some condition remains true

name = input("Enter your name: ")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("Enter your age: "))
while age < 0:
    print("Age can't be nagative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

num = int(input("Enter a number between 1 to 10"))
while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a number between 1 to 10"))
print(f"Your number is {num}")

food = input("Enter a food you lik (q to quit)")
while not food == "q":
    print(f"you like {food})")
    food = input("Enter another food you lik (q to quit)")
print(f"Bye {name}")