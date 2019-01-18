ulist = list(map(int, input().split(" ")))
for i in range(len(ulist)-1, 0, -1):
    while ulist[i-1] > ulist[i]:
        ulist[i-1], ulist[i] = ulist[i], ulist[i-1]
        if i < len(ulist)-1:
            i+=1
# temp = ulist.pop()
# ulist.insert(0, temp)
for el in ulist:
    print(el, end=" ")
