n = int(input())
m = int(input())
com = 0
while not m == 0:
    com = m
    m = n%m
    n = com
print(n)