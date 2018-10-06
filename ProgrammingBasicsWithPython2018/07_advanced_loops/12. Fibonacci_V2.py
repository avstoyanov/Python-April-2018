#series soultuion
n = int(input())
cur = 1
curr = 1
if n < 2:
    n = 1
else:
    for num in range(1, n):
        n = cur + curr
        cur = curr
        curr = n
print(n)