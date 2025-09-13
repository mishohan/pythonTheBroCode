# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) #1
print(credit_number[1]) #2
print(credit_number[2]) #3
print(credit_number[3]) #4
print(credit_number[4]) #-

print(credit_number[ : 4]) # 1234 #The ending idex(4) is exclusive...index[0 1 2 3]
print(credit_number[5 : 9]) # 5678
print(credit_number[5 :]) # 5678-9012-3456

print(credit_number[-1]) #6
print(credit_number[-2]) #5
print(credit_number[-3]) #4
print(credit_number[-4]) #3
print(credit_number[-5]) #-

print(credit_number[:: 2]) #13-6891-46

# Practical Example
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}") # XXXX-XXXX-XXXX-3456

# Another Example
credit_number = credit_number[:: -1]
print(credit_number) # 6543-2109-8765-4321