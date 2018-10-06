fruit = input().lower()
day = input().lower()
amount = float(input())
price = 0
printy = 0
if day == "sunday" or day == "saturday":
    if fruit == "banana":
        price = 2.7
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.9
    elif fruit == "grapefruit":
        price = 1.6
    elif fruit == "kiwi":
        price = 3
    elif fruit == "pineapple":
        price = 5.6
    elif fruit == "grapes":
        price = 4.2
    else:
        printy = "Error"

elif day == "monday" or day == "tuesday" or day == "wednesday" or day == "thursday" or day == "friday":
    if fruit == "banana":
        price = 2.5
    elif fruit == "apple":
        price = 1.2
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.7
    elif fruit == "pineapple":
        price = 5.5
    elif fruit == "grapes":
        price = 3.85
    else:
        printy = "Error"
else:
    printy = "Error"
if not printy == "Error":
    print("{0:.2f}".format(price * amount))
else:
    print(printy)