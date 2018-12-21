int_list = sorted(list(map(int, input().split(" "))))
simp = []
for each in int_list:
    if each not in simp:
        simp.append(each)
        print(each, "->", int_list.count(each))
