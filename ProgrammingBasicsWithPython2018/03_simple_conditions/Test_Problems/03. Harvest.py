import math

area = int(input())
gPM = float(input())
amount = int(input())
workers = int(input())
wineArea = area * 0.4
grapes = wineArea*gPM
litersWine = grapes/2.5
if litersWine < amount:
    print("It will be a tough winter! More", int(amount - litersWine), "liters wine needed.")
else:
    print("Good harvest this year! Total wine:", int(litersWine), "liters.")
    print(math.ceil(litersWine - amount), "liters left ->", math.ceil((litersWine-amount)/workers), "liters per person.")