# Area of a Circle

import math

radius = float(input("Enter the radius of a circle: "))

area = math.pi * math.pi * pow(radius, 2)

print(f"The area of the circle is: {round(area, 4)}cm²")