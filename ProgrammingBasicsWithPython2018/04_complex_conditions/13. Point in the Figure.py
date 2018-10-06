h = int(input())
x = int(input())
y = int(input())
if 0 <= x <= 3*h:
    if 0 <= y <= h:
        if x == 0 or x == 3*h or y == 0:
            print("border")
        elif (0 <= x <= h and y == h) or (2*h <= x <= 3*h and y == h):
            print("border")
        else:
            print("inside")
    elif h <= y <= 4*h:
        if h <= x <= 2*h:
            if x == h or x == 2*h or y == 4*h:
                print("border")
            else:
                print("inside")
        else:
            print("outside")
    else:
        print("outside")
else:
    print("outside")