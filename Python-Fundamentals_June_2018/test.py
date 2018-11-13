mylist = ["dress", "t-shirt", "boxers", "hat", "hat", "boxers"]
newlist = []
for item in mylist:
    final_string = item + ' - ' + str(mylist.count(item))
    if final_string not in newlist:
        newlist.append(final_string)


print(newlist)

