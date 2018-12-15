data_l = list(map(float, input().split(" ")))
i = 0
while i < len(data_l)-1:
    if data_l[i] == data_l[i+1] and i >= 0:
        data_l[i] += data_l[i+1]
        data_l.remove(data_l[i+1])
        i -= 1
    else:
        i += 1
# print(f'{" ".join(list(map(str, data_l)))}'.format)

for sasho in data_l:
    print("{:g}".format(sasho), end=" ")
