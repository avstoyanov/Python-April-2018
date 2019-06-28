raw_Input = input()
topic_Dict = {}
while raw_Input != "filter":
    topic, tags = raw_Input.split(" -> ")
    if topic not in topic_Dict:
        topic_Dict[topic] = []
    for elems in tags.split(", "):
        if elems not in topic_Dict[topic]:
            topic_Dict[topic].append(elems)
    raw_Input = input()

filters_List = input().split(", ")
for terms in topic_Dict:
    for filt in filters_List:
        if filt not in topic_Dict[terms]:
            topic_Dict[terms] = []
            break

for elements in topic_Dict:
    if topic_Dict[elements]:
        print(elements + " | ",end="")
        for things in topic_Dict[elements]:
            if things != topic_Dict[elements][-1]:
                print("#"+things,end=", ")
            else:
                print("#"+things)
