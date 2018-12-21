num_list = list(map(int, input().split(" ")))
min = num_list[0]
for nums in num_list:
    if nums < min:
        min = nums
print(min)
