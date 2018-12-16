num_list = list(map(int, input().split(" ")))
rev_list = []

for elem in num_list:
    if elem > 0 and pow(elem, 0.5) % 1 == 0:
        rev_list.append(elem)
rev_list.sort(reverse=True)
for res in rev_list:
    print(res, end=" ")
