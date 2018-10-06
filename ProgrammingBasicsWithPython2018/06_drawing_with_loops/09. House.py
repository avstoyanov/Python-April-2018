num = int(input())
for row in range(1, (num + 1) // 2 + 1):
    if num % 2 == 0:
        print("-" * ((num // 2) - row) + "**" * row + "-" * ((num // 2) - row))
    else:
        print("-" * ((num // 2) - row + 1) + "*" * (2 * row - 1) + "-" * ((num // 2) - row + 1))
for row in range(num // 2):
    print("|" + "*" * (num - 2) + "|")