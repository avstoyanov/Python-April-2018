raw_inp = input()
cities = {}

while raw_inp != "ready":
    city, transport = raw_inp.split(":")
    listrans = transport.split(",")
    if city not in cities:
        cities[city] = {}
    for items in listrans:
        trans, seats = items.split("-")
        cities[city][trans] = int(seats)
    raw_inp = input()

raw_inp = input()
while raw_inp != "travel time!":
    dest_city, people_count = raw_inp.split()
    people_count = int(people_count)
    total_seats = 0
    for trans_type in cities[dest_city]:
        total_seats += cities[dest_city][trans_type]
    if total_seats >= people_count:
        print(f"{dest_city} -> all {people_count} accommodated")
    else:
        print(f"{dest_city} -> all except {people_count - total_seats} accommodated")
    raw_inp = input()
