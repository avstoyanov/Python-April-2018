city = input().lower()
amount = float(input())
if city == "sofia":
    if 0 <= amount <= 500:
        amount = amount * 0.05
    elif 500 < amount <= 1000:
        amount = amount * 0.07
    elif 1000 < amount <= 10000:
        amount = amount * 0.08
    elif 10000 < amount:
        amount = amount * 0.12
    else:
        print("error")
elif city == "varna":
    if 0 <= amount <= 500:
        amount = amount * 0.045
    elif 500 < amount <= 1000:
        amount = amount * 0.075
    elif 1000 < amount <= 10000:
        amount = amount * 0.1
    elif 10000 < amount:
        amount = amount * 0.13
    else:
        print("error")
elif city == "plovdiv":
    if 0 <= amount <= 500:
        amount = amount * 0.055
    elif 500 < amount <= 1000:
        amount = amount * 0.08
    elif 1000 < amount <= 10000:
        amount = amount * 0.12
    elif 10000 < amount:
        amount = amount * 0.145
    else:
        print("error")
else:
    print("error")
print("{0:.2f}".format(amount))