num = int(input())
for row in range((num + 1) // 2):
    if num % 2 == 0:
        print("-" * ((num // 2) - row) + "*" + "--" * row + "*" + "-" * ((num // 2) - row))
    else:
        print("-" * ((num // 2) - row) + "*" + "-" * (row*2 - 1) + "*" * ((row + 1) // num) + "-" * ((num // 2) - row))
for row in range(num // 2):
    if num % 2 == 0:
        print("-" * (row + 1) + "*" + "--" * (num // 2 - 2 - row) + "*" + "-" * (row + 1))
    else:
        print("-" * (row + 1) + "*" + "--" * (num // 2 - 2 - row) * ((row + 1) // num) + "-*" * ((row + 1) // num) + "-" * (row + 1))
