num_list = list(map(int, input().split(" ")))
num_list.sort()
print(num_list[0], end="")
num_list.remove(num_list[0])
for element in num_list:
    print(" <= " + str(element), end="")
