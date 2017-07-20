# TILING CALCULATOR
# Calculate the total cost of tile it would take,
# to cover a floor plan of width and height, using a cost entered by the user.

width = float(raw_input("Room width (cm):"))
height = float(raw_input("Room height (cm):"))
cost = float(raw_input("Cost per m^2: "))

Total_cost = width*height/(100.0**2)*cost
print "Total cost of tiling is: $%.2f" % Total_cost

