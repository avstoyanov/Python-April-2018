unsrtd_list = list(map(int, input().split(" ")))
sortd = False
while not sortd:
    sortd = True
    for item in range(len(unsrtd_list)-1):
        if unsrtd_list[item] > unsrtd_list[item+1]:
            unsrtd_list[item], unsrtd_list[item+1] = unsrtd_list[item+1], unsrtd_list[item]
            sortd = False
for el in unsrtd_list:
    print(el, end=" ")
