ticket = input().lower()
rows = int(input())
columns = int(input())
profit = 0
if ticket == "premiere":
    profit = rows*columns*12
elif ticket == "normal":
    profit = rows*columns*7.5
elif ticket == "discount":
    profit = rows*columns*5
print("{0:.2f} leva".format(profit))