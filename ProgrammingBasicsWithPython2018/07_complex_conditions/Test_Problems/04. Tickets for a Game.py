budget = float(input())
category = input().lower()
people = int(input())
vip = 499.99
normal = 249.99
transport = 0
if 1 <= people <= 4:
    transport = budget*0.75
elif 5 <= people <= 9:
    transport = budget*0.6
elif 10 <= people <= 24:
    transport = budget*0.5
elif 25 <= people <= 49:
    transport = budget*0.4
else:
    transport = budget*0.25

moneyLeft = budget - transport
moneyNeeded = float(eval(category))*people

if moneyLeft > moneyNeeded:
    print("Yes! You have {0:.2f} leva left.".format(moneyLeft-moneyNeeded))
else:
    print("Not enough money! You need {0:.2f} leva.".format(moneyNeeded-moneyLeft))