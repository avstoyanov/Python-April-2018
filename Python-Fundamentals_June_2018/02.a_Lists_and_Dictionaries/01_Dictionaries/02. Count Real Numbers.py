nums_list = list(map(float, input().split(" ")))
dict_nums = {}
for term in nums_list:
    if term not in dict_nums:
        dict_nums[term] = 0
    dict_nums[term] += 1
sort_dict = sorted(dict_nums)
for item in sort_dict:
    print(f"{item} -> {dict_nums[item]} times")
