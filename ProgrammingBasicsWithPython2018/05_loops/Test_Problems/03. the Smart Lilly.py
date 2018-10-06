age = int(input())
goal = float(input())
tPrice = int(input())
gMoney = 0
tMoney = 0
for num in range(1, age + 1):
    if num % 2 == 0:
        #on every second birthday, the money recieved is increased by 10, ex.(2nd = 10, 4th = 20, total= 30) minus the money for brother
        gMoney += 10*(num/2) - 1
    else:
        tMoney += tPrice
totalMoney = tMoney + gMoney
if totalMoney >= goal:
    print("Yes! {:.2f}".format(totalMoney - goal))
else:
    print("No! {:.2f}".format(goal-totalMoney))
