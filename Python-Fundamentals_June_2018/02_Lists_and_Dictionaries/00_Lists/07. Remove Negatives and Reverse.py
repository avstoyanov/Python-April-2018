num_list = list(map(int, input().split(" ")))
ans_list = []
for item in (num_list):
    if item >= 0:
        ans_list.append(item)
if len(ans_list) == 0:
    print("empty")
else:
    ans_list.reverse()
    for num in ans_list:
        print(num, end=" ")
