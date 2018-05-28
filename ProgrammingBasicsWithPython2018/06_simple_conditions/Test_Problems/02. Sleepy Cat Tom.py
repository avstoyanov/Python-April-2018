days_off = int(input())
workdays = 365-days_off
playtime = 127*days_off + 63*workdays
diff = abs(30000 - playtime)
hrsDiff = diff // 60
minutesDiff = diff % 60
if playtime < 30000:
    print("Tom sleeps well")
    print(hrsDiff, "hours and", minutesDiff, "minutes less for play")
else:
    print("Tom will run away")
    print(hrsDiff, "hours and", minutesDiff, "minutes more for play")
