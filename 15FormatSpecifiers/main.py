# format specifiers = {value:flags} format a value based on what flag are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 3123.14159
price2 = -9870.65
price3 = 2235.34

print(f"price1 is ${price1}")
print(f"price2 is ${price2}")
print(f"price3 is ${price3}")

# fixed decimal places
print(f"price1 is ${price1 :.1f}")
print(f"price2 is ${price2 :.1f}")
print(f"price3 is ${price3 :.1f}")

# Allocate spaces
print(f"price1 is ${price1 :10.2f}")
print(f"price2 is ${price2 :010.2f}")
print(f"price3 is ${price3 :<10.2f}") # Left justify
print(f"price3 is ${price3 :>10.2f}") # Right justify
print(f"price3 is ${price3 :^10.2f}") # Center Align

# Indicating Positive Value for all positive numbers
print(f"price1 is ${price1 :+10.1f}")
print(f"price2 is ${price2 :+10.1f}")
print(f"price3 is ${price3 : 10.1f}") # can also use a space instead of a + (don't!)

# Thousand Separator
print(f"price1 is ${price1 :+10,.2f}")
print(f"price2 is ${price2 :+10,.2f}")
print(f"price3 is ${price3 :+10,.2f}")