# create point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# define distance function
def CalcDistance(p1, p2):
    a = p1.x - p2.x
    b = p1.y - p2.y
    return pow((pow(a, 2) + pow(b, 2)), 0.5)


# take inputs
raw_p1 = input()
raw_p2 = input()

# split input into coordinates
x1, y1 = raw_p1.split(" ")
x2, y2 = raw_p2.split(" ")

# define points
point1 = Point(int(x1), int(y1))
point2 = Point(int(x2), int(y2))

# get distance
print(f"{CalcDistance(point1, point2):.3f}")
