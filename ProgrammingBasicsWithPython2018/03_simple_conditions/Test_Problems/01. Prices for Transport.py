km = int(input())
time = input()
price = 0
if km < 20:
    if time == "day":
        price = 0.7 + km * 0.79
    else:
        price = 0.7 + km * 0.9
elif 20 <= km < 100:
    price = km * 0.09
else:
    price = km * 0.06
print(price)