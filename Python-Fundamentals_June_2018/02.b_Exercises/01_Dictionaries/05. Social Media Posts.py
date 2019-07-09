data_dic = {}
raw_data = input()

while raw_data != "drop the media":
    list_data = raw_data.split(" ")
    type_data = list_data[0]
    post = list_data[1]
    if type_data == "post":
        data_dic[post] = {}
        data_dic[post]['like'] = 0
        data_dic[post]['dislike'] = 0
        data_dic[post]['comment'] = []
    elif type_data != "comment":
        data_dic[post][type_data] += 1
    else:
        name = list_data[2]
        comment = " ".join(list_data[3:])
        data_dic[post][type_data].append(f"*  {name}: {comment}")
    raw_data = input()

for item in data_dic:
    print(f"Post: {item} | Likes: {data_dic[item]['like']} | Dislikes: {data_dic[item]['dislike']}")
    print("Comments: ")
    if data_dic[item]["comment"]:
        for each in data_dic[item]["comment"]:
            print(each)
    else:
        print("None")

#dadfafdafafafa