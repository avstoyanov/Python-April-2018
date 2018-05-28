hours = int(input())
minutes = int(input())
inMin = hours*60 + minutes + 15
endHours = (inMin // 60) % 24
endMin = inMin % 60
if endMin < 10:
    endMin = "0" + str(endMin)
print(str(endHours) + ":" + str(endMin))
