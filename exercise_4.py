"""4. Write a Python program which accepts the radius of a circle from the user and compute the area."""
import math
r=float(input('Enter the radius: '))

area=math.pi*(r**2)

print('The area of the circle with radius {} is {:.2f}'.format(r,area))