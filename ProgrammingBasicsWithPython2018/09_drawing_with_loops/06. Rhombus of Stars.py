num = int(input())
for row in range(1, num + 1):
    print(" " * (num - row) + "* " * row)
for row in range(1, num):
    print(" " * row + "* " * (num - row))
