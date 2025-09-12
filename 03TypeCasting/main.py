#Typecasting = the process of converting a variable from one data type to another
#              str(), int(), float(), bool()

name = "MI Shohan"
age = 25
gpa = 3.7
is_student = True

# Datatype
print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(gpa)) # <class 'float'>
print(type(is_student)) # <class 'bool'>

NAME = bool(name)
AGE = float(age)
GPA = int(gpa)

print(type(NAME)) # <class 'bool'>
print(NAME) # True
print(type(AGE)) # <class 'float'>
print(type(GPA)) # <class 'int'>

Age = 25
Age = str(Age)
Age += "1"
print(Age) # 251

Name = ""
Name = bool(Name)
print(Name) # False