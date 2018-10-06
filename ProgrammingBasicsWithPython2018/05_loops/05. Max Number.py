numOfNums = int(input())
max = int(input())
for num in range(1, numOfNums):
    curr = int(input())
    if max < curr:
        max = curr
print(max)