n = int(input())


def triangle(num):
    for row in range(1, num + 1):
        print(row,end=" ")


for i in range(1, 2*n):
    if i <= n:
        triangle(i)
    else:
        triangle(i-n)
