numOfNums = int(input())
max = int(input())
sum = max
for num in range(1, numOfNums):
    curr = int(input())
    sum += curr
    if max < curr:
        max = curr
if max == (sum - max):
    print("Yes Sum =", max)
else:
    print("No Diff =", abs((sum-max)-max))