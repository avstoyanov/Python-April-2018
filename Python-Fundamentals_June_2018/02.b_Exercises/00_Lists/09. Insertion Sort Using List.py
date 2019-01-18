ulist = list(map(int, input().split(" ")))
flist = []
flist.append(ulist.pop(0))
for ele in range(len(ulist)):
    for num in range(len(flist)):
        if ulist[ele] not in flist:
            if ulist[ele] < flist[num]:
                flist.insert(num, ulist[ele])
            elif num == len(flist)-1:
                flist.append(ulist[ele])
for elm in flist:
    print(elm, end=" ")
