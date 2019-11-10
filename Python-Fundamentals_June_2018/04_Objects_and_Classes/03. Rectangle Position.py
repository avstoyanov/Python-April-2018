# create point class (see 01. Distance between points)
class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

#define a rectangle
def rectangle(left, top, width, height):
    top_left = Point(left, top) #define parameters as points
    bottom_right = Point((int(left) + width), (int(top) - height))
    rect = [top_left, bottom_right]
    return rect

#define is_inside
def is_inside(rect1, rect2):
    # rename parameters for the rectangle
    top_left1 = rect1[0]
    bottom_right1 = rect1[1]
    top_left2 = rect2[0]
    bottom_right2 = rect2[1]
    #check if second rectangle contains the first
    if top_left1.x >= top_left2.x and bottom_right1.x <= bottom_right2.x:
        if top_left1.y <= top_left2.y and bottom_right1.y >= bottom_right2.y:
            return "Inside"
        else:
            return "Not inside"
    else:
        return "Not inside"

#format input into input for rectangle method
left1, top1, w1, h1 = input().split(" ")
left2, top2, w2, h2 = input().split(" ")
#assign names to the two rectangles inputted
rect1 = rectangle(left1, top1, int(w1), int(h1))
rect2 = rectangle(left2, top2, int(w2), int(h2))
#print results
print(is_inside(rect1, rect2))
