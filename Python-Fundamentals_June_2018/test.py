my_list1 = [3, 4, 6, 12, 3]

print("list 1, ", id(my_list1))

new_list = my_list1
print("list 2, ", id(new_list))

new_list_v2 = my_list1.copy()

print("list 1, ", id(my_list1))

print("list 2, ", id(new_list))
print("list 3, ", id(new_list_v2))

print("list 3, ", new_list_v2)
