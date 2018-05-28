num = int(input())
if 1 <= num <= 7:
    weekdays = ["Mon", "Tues", "Wednes", "Thurs", "Fri", "Satur", "Sun"]
    day = weekdays[num-1]
    print(day + "day")
else:
    print("Error")