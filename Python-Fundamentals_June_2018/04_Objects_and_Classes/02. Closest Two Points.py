# create point class
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# define distance function
def calc_distance(p1, p2):
    a = int(p1.x) - int(p2.x)
    b = int(p1.y) - int(p2.y)
    return pow((pow(a, 2) + pow(b, 2)), 0.5)
#end of distance calculation

#define the minimum distance function
def min_distance(point_list):
    min_dist = calc_distance(point_list[0], point_list[1])
    min_pair1 = point_list[0]
    min_pair2 = point_list[1]

#find distance between each point and compare for length
    while len(point_list) != 0: #while is used in order to edit list length while retaining order of elements
        point = point_list[0] #assigns first term to var point
        del point_list[0] #shortens comparisons, reducing repetition by approximately 50%
        for elem in point_list:
            dist = calc_distance(point, elem) #compares first(deleted) element of list with all others
            if dist < min_dist: #finds lowest distance and assigns points it is comprised of
                min_dist = dist
                min_pair1 = point
                min_pair2 = elem
    return f"{min_dist:.3f};({min_pair1.x}, {min_pair1.y});({min_pair2.x}, {min_pair2.y})"
#end of min_distance

pnt_list = []
# take inputs
n = input()
for pt in range(int(n)):
    x, y = input().split(" ")
    pnt_list.append(Point(x, y))
#print results
min, p1, p2 = min_distance(pnt_list).split(";")
print(min)
print(p1)
print(p2)
