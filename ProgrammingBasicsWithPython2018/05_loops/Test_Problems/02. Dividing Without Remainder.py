numbers = int(input())
cat1 = 0
cat2 = 0
cat3 = 0
for num in range(0, numbers):
    curr = int(input())
    if curr % 2 == 0:
        cat1 += 1
    if curr % 3 == 0:
        cat2 += 1
    if curr % 4 == 0:
        cat3 += 1
print("{:.2f}%".format(100 * cat1/numbers))
print("{:.2f}%".format(100 * cat2/numbers))
print("{:.2f}%".format(100 * cat3/numbers))