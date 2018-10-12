n = int(input())


def triangle(num):
    for row in range(1, num + 1):
        print(row,end=" ")


for i in range(n - 1, -n, -1):
    print()
    triangle(n - abs(i))
