# for loops = execute a block of code a fixed number of times.
#             you can iterate over a range, strign, sequence, etc.


# Basic format: iterating in a given range
for X in range(1, 11):
    print(X)
print("Happy New Year!")

for X in reversed(range(1, 11)):
    print(X)
print("Happy New Year!")

for X in (range(1, 11, 2)):
    print(X)
print("Happy New Year!")

for X in reversed(range(1, 11, 2)):
    print(X)
print("Happy New Year!")


# Iterating over string
credit_card = "1234-5678-9012-3456"

for X in credit_card:
    print(X)
print("Happy New Year!")

for X in reversed(credit_card):
    print(X)
print("Happy New Year!")


# Two Keywords(continue, break)
for X in range(1, 21):
    if X == 13:
        continue
    else:
        print(X)
print("Happy New Year!")

for X in range(1, 21):
    if X == 13:
        break
    else:
        print(X)
print("Happy New Year!")