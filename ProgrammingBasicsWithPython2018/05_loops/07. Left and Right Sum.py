nums = int(input())
sum1 = 0
sum2 = 0
for num in range(0, nums*2):
    curr = int(input())
    if num < nums:
        sum1 += curr
    else:
        sum2 += curr
if sum1 == sum2:
    print("Yes, sum =", sum1)
else:
    print("No, diff =", abs(sum1 - sum2))