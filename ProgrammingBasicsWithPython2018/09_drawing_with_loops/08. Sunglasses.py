num = int(input())
print("*" * (2 * num) + " " * num + "*" * (2 * num))
for row in range(1, num - 1):
    if (num % 2 == 0 and row == (num / 2) - 1) or (not (num % 2 == 0) and row == (num - 1) / 2):
        print("*" + "/" * (2 * (num - 1)) + "*" + "|" * num + "*" + "/" * (2 * (num - 1)) + "*")
    else:
        print("*" + "/" * (2 * (num - 1)) + "*" + " " * num + "*" + "/" * (2 * (num - 1)) + "*")
print("*" * (2 * num) + " " * num + "*" * (2 * num))
