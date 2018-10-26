int_list = list(map(int, input().split(" ")))
min = int_list[0]
for num in int_list:
    if min > num:
        min = num
print(min)
