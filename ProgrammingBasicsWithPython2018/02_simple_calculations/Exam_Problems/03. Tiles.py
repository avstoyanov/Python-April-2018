l_O_Y = float(input())
l_O_T = float(input())
w_O_T = float(input())
l_O_B = float(input())
w_O_B = float(input())
tot_Area = l_O_Y * l_O_Y
area_For_Tiles = tot_Area - (w_O_B * l_O_B)
num_Tiles = area_For_Tiles/(l_O_T * w_O_T)
time_needed = num_Tiles * 0.2
# 0.2 being minutes per tile
print("%.2f" % num_Tiles)
print("%.2f" % time_needed)