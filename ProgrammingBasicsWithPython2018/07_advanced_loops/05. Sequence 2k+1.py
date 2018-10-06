n = int(input())
curr = 0
for num in range(0, n+1):
    if curr*2 +1 == num:
        print(num)
        curr = num
