lst = input().split(" ")
n = input()
is_the_int_in_the_list = False
for each in lst:
    if n == each:
        is_the_int_in_the_list = True
        break
if is_the_int_in_the_list == True:
    print("yes")
else:
    print("no")
