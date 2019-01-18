ulist = list(map(int, input().split(" ")))
for i in range(1, len(ulist)):
    while ulist[i] < ulist[i-1] and i > 0:
        ulist[i], ulist[i-1] = ulist[i-1], ulist[i]
        i-=1
for el in ulist:
    print(el, end=" ")
