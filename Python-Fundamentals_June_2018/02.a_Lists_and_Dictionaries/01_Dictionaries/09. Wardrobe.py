clothes = {}
colors = int(input())
for item in range(colors):
    raw = input()
    color, cloth = raw.split(" -> ")
    if color not in clothes:
        stufflist = cloth.split(",")
        clothes[color] = stufflist
    else:
        for its in cloth.split(","):
            clothes[color].append(its)

search = input()
search_item_list = search.split(' ')
for place in clothes.keys():
    simplist = []
    print(f"{place} clothes:")
    for spot in clothes[place]:
        for item in clothes[place]:
            final_string = item + ' - ' + str(clothes[place].count(item))
            if final_string not in simplist:
                simplist.append(final_string)
    for iter in simplist:
        if search_item_list[1] in iter and search_item_list[0] == place and len(search_item_list) == 2:
            print("* " + iter + " (found!)")
        else:
            print("* " + iter)
