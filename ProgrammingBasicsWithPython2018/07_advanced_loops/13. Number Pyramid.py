n = int(input())
cur = 0
cur1 = 0
while cur < n:
    cur1 += 1
    for num in range(0, cur1):
        cur += 1
        print(cur, end=" ")
        if cur == n:
            break
    print()
