t1 = int(input())
t2 = int(input())
t3 = int(input())
sum = t1 + t2 + t3
sIMR = str(sum % 60)
sIM = str(sum // 60)
if int(sIMR) < 10:
    sIMR = "0" + sIMR
print(sIM + ":" + sIMR)
