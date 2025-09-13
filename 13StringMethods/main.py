# String Methods

name = input("Enter Your full name: ")
phone_number = input("Enter your phone number: ")

# Length of a String
result1 = len(name)
print(result1)

# find method: first occurance of a character
result2 = name.find(" ")
print(result2)

# reverse find method: last occurance of a character
result3 = name.rfind("l")
print(result3)
# if doesn't able to find character, returns -1

# capitalizing: only the first letter
capital = name.capitalize()
print(capital)

# upper method
uppercase = name.upper()
print(uppercase)

# lower method
lowercase = name.lower()
print(lowercase)

# isdigit() retuns true or false : only for digits(123) return true
is_digit = name.isdigit()
print(is_digit)

# isalpha() method: only for alphabetical character returns true
is_alpha = name.isalpha()
print(is_alpha)

# count() method:
phone = phone_number.count("-")
print(phone)

# replace() method:
replaced = phone_number.replace("-", " ")
print(replaced)

# To get all the methods available
# print(help(str))
# doesn't work on vs code