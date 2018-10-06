neededHours = int(input())
days = int(input())
workers = int(input())
realDays = days*0.9
hoursWork = realDays*8 + workers*(2*days)
totalHours = int(hoursWork)
if totalHours < neededHours:
    print("Not enough time!" + str(neededHours - totalHours), "hours needed.")
else:
    print("Yes!" + str(totalHours - neededHours), "hours left.")