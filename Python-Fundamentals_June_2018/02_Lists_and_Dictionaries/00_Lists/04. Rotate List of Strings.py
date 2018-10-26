rot_list = list(input().split(" "))
last = rot_list.pop()
rot_list.insert(0, last)
for ele in rot_list:
    print(ele, end=" ")
