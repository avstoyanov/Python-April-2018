n = int(input())
leftright = (n-1)//2
mid = n-2 * leftright - 2

for leftright in range(leftright, 0, -1):
    if mid < 0:
        print("-" * leftright + "*" + "-" * leftright)
    else:
        print("-" * leftright + "*" + "-" * mid + "*" + "-" * leftright)

    mid += 2

for leftright in range((n + 1)//2):

    if mid < 0:
        print("-" *leftright + "*" + "-" * leftright)
    else:
        print("-" * leftright + "*" + "-" * mid + "*" + "-" * leftright)

    mid -= 2