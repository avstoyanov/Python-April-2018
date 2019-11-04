# create point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# define distance function
def CalcDistance(p1, p2):
    a = int(p1.x) - int(p2.x)
    b = int(p1.y) - int(p2.y)
    return pow((pow(a, 2) + pow(b, 2)), 0.5)
#end of distance calculation

point_list = []
# take inputs
n = input()
for pt in range(int(n)):
    x, y = input().split(" ")
    point_list.append(Point(x, y))

#define the minimum distance and points which it corrisponds to
min_dist = CalcDistance(point_list[0], point_list[1])
min_pair1 = point_list[0]
min_pair2 = point_list[1]

#find distance between each point and compare for length
i = 0
while len(point_list) != 0:
    point = point_list[i]
    del point_list[i]
    for elem in point_list:
        dist = CalcDistance(point, elem)
        if dist < min_dist:
            min_dist = dist
            min_pair1 = point
            min_pair2 = elem
#print results
print(f"{min_dist:.3f}")
print(f"({min_pair1.x}, {min_pair1.y})")
print(f"({min_pair2.x}, {min_pair2.y})")
