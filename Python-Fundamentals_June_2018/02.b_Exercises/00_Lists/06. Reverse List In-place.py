raw_list = input().split(" ")
for elem in range(int(len(raw_list)/2)):
    raw_list[elem], raw_list[-(elem+1)] = raw_list[-(elem+1)], raw_list[elem]
for nums in raw_list:
    print(nums, end=" ")
