str_list = input().lower().split(" ")
dict_str = {}
for item in str_list:
    if item in dict_str:
        dict_str[item] += 1
    else:
        dict_str[item] = 1
liststr = []
for item in dict_str:
    if dict_str[item]%2 != 0:
        liststr.append(item)
print(", ".join(liststr))
