test_hour = int(input())
test_minute = int(input())
arrive_hour = int(input())
arrive_min = int(input())
test_time = test_hour*60 + test_minute
arrive_time = arrive_hour*60 + arrive_min
total_mins = abs(test_time - arrive_time)
mins = total_mins % 60

if  test_time - arrive_time > 30:
    if (mins) < 10:
        mins = "0" + str(mins)
    print("Early")
    if total_mins >= 60:
        print(str((total_mins)//60) + ":" + str(mins) + " hours before the start")
    else:
        print(str(mins) + "minutes before the start")
elif 0 <= (test_time - arrive_time) <= 30:
    print("On time")
    print(str(mins) + "minutes before the start")
else:
    print("Late")
    if total_mins >= 60:
        if (mins) < 10:
            mins = "0" + str(mins)
        print(str((total_mins)//60) + ":" + str(mins) + " hours after the start")
    else:
        print(str(mins) + "minutes after the start")