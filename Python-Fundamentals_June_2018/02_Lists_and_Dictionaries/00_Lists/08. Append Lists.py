num_list = input().split("|")
num_list.reverse()
tot_string = ""
for ele in num_list:
    tot_string += ele + " "
raw_list = tot_string.split(" ")
for place in raw_list:
    if place != "":
        print(place, end=" ")
