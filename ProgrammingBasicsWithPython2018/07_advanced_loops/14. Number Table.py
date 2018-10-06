n = int(input())
ans = 0
for col in range(0, n):
    for row in range(0,n):
        ans = row + col + 1
        if ans <= n:
            print(ans, end=" ")
        else:
            print(2*n - ans, end=" ")
    print()
