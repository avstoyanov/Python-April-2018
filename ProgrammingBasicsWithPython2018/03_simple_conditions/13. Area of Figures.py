import math

shape = input()
if shape == "square":
    side = float(input())
    answer = side*side
elif shape == "rectangle":
    length = float(input())
    hght = float(input())
    answer = length*hght
elif shape == "circle":
    radius = float(input())
    answer = math.pi * radius *radius
else:
    base = float(input())
    hght = float(input())
    answer = base * hght/2
print("{0:.3f}".format(answer))