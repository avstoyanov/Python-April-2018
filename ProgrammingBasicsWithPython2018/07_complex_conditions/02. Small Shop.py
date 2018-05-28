product = input().lower()
city = input().lower()
amount = float(input())
price = 0
if city == "sofia":
    if product == "coffee":
        price = 0.5 * amount
    elif product == "water":
        price = 0.8 * amount
    elif product == "beer":
        price = 1.2 * amount
    elif product == "sweets":
        price = 1.45 * amount
    else:
        price = 1.6 * amount
elif city == "plovdiv":
    if product == "coffee":
        price = 0.4 * amount
    elif product == "water":
        price = 0.7 * amount
    elif product == "beer":
        price = 1.15 * amount
    elif product == "sweets":
        price = 1.3 * amount
    else:
        price = 1.5 * amount
else:
    if product == "coffee":
        price = 0.45 * amount
    elif product == "water":
        price = 0.7 * amount
    elif product == "beer":
        price = 1.1 * amount
    elif product == "sweets":
        price = 1.35 * amount
    else:
        price = 1.55 * amount

print("{0:.2f}".format(price))
