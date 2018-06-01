numOfNums = int(input())
min = int(input())
for num in range(1, numOfNums):
    curr = int(input())
    if min > curr:
        min = curr
print(min)