length = float(input())
startT = input()
endT = input()
milli = 1/1000
centi = 1/100
miles = 1/ 0.000621371192
inch = 1/39.3700787
kilom = 1/0.001
feet = 1/3.2808399
yard = 1/1.0936133
curr = 0
if startT == "mm":
    curr = milli*length
elif startT == "m":
    curr = length
elif startT == "cm":
    curr = centi*length
elif startT == "mi":
    curr = miles*length
elif startT == "in":
    curr = inch*length
elif startT == "km":
    curr = kilom*length
elif startT == "ft":
    curr = feet*length
elif startT == "yd":
    curr = yard*length
#############################################
if endT == "mm":
    curr = curr*(1/milli)
elif endT == "cm":
    curr = curr*(1/centi)
elif endT == "mi":
    curr = curr*(1/miles)
elif endT == "in":
    curr = curr*(1/inch)
elif endT == "km":
    curr = curr*(1/kilom)
elif endT == "ft":
    curr = curr*(1/feet)
elif endT == "yd":
    curr = curr*(1/yard)
print(curr, endT)