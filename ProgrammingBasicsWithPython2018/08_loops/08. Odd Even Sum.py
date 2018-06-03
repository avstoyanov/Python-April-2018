nums = int(input())
sum1 = 0
sum2 = 0
for num in range(0, nums):
    curr = int(input())
    if num % 2 == 0:
        sum2 += curr
    else:
        sum1 += curr
if sum1 == sum2:
    print("Yes Sum =", sum1)
else:
    print("No Diff =", abs(sum1-sum2))