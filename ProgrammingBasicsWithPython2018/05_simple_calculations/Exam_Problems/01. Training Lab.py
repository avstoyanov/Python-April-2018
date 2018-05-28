length = float(input())*100
width = float(input())*100
desk_W = 70
desk_L = 120
num_of_columns = int((width - 100) / desk_W)
num_of_rows = int(length / desk_L)
num_of_desks = (num_of_columns * num_of_rows) - 3
print (num_of_desks)
