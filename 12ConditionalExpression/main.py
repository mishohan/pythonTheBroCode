# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                          X if condition else Y

num1 = -5
print("Positive" if num1 > 0 else "Negative") # Negative

num2 = 6
result = "Even" if num2 % 2 == 0 else "Odd"
print(result) # Even

a = 6
b = 7
max_num = a if a>b else b
min_num = a if a<b else b
print(max_num) # 7
print(min_num) # 6

age = 25
status = "Adult" if age >= 18 else "Child"
print(status) # Adult

temperature = 30
weather = "HOT" if temperature>20 else "COLD"
print(weather) # HOT

user_role = "Admin"
access_level = "Full Access" if user_role == "Admin" else "Limited Access"
print(access_level) #Full Access