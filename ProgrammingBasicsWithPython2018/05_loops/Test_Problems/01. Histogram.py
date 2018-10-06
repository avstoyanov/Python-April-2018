numbers = int(input())
cat1 = 0
cat2 = 0
cat3 = 0
cat4 = 0
cat5 = 0
for num in range(0, numbers):
    curr = int(input())
    if curr < 200:
        cat1 += 1
    elif 200 <= curr < 400:
        cat2 += 1
    elif 400 <= curr < 600:
        cat3 += 1
    elif 600 <= curr < 800:
        cat4 += 1
    else:
        cat5 += 1
print(str(100 * cat1/numbers) + "%")
print(str(100 * cat2/numbers) + "%")
print(str(100 * cat3/numbers) + "%")
print(str(100 * cat4/numbers) + "%")
print(str(100 * cat5/numbers) + "%")


