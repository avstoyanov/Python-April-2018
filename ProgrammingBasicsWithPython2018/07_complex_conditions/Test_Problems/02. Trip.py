budget = float(input())
season = input().lower()
location = ""
place = ""
if season == "winter":
    place = "Hotel -"
else:
    place = "Camp -"
if budget <= 100:
    location = "Somewhere in Bulgaria"
    if season == "winter":
        budget = budget*0.7
    else:
        budget = budget*0.3
elif budget <=1000:
    location = "Somewhere in Balkans"
    if season == "winter":
        budget = budget * 0.8
    else:
        budget = budget * 0.4
else:
    location = "Somewhere in Europe"
    budget = budget*0.9
    place = "Hotel -"
print(location)
print(place, "{0:.2f}".format(budget))
