month = input().lower()
nights = int(input())
studio = 0
apartment = 0
if month == "may" or month == "october":
    if nights > 7:
        if nights > 14:
            apartment = 65 * 0.9
            studio = 50*0.7
        else:
            studio = 50 * 0.95
            apartment = 65
    else:
        studio = 50
        apartment = 65
elif month == "june" or month == "september":
    if nights > 14:
        apartment = 68.7 * 0.9
        studio = 75.2*0.8
    else:
        studio = 75.2
        apartment = 68.7
else:
    if nights > 14:
        apartment = 77 * 0.9
    else:
        apartment = 77
    studio = 76
print("Apartment:", "{0:.2f}".format(apartment*nights), "lv.")
print("Studio:", "{0:.2f}".format(studio*nights), "lv.")