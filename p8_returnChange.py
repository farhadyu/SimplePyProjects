# The user enters a cost and then the amount of money given.
# The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

cost = float(raw_input("Total Cost: $"))
payed = float(raw_input("Amount payed: $"))
change = payed - cost
print change
quarters = 0
dimes = 0
nickels = 0
pennies = 0
change = int(change*100)
while change > 0:
    if change >= 25:
        quarters += 1
        change -= 25
    elif change >= 10:
        dimes += 1
        change -= 10
    elif change >= 5:
        nickels += 1
        change -= 5
    elif change >= 1:
        pennies += 1
        change -= 1
    else:
        print "Error"
        break

print "\nYour change is:"
print "Quarters: %d" % quarters
print "Dimes: %d" % dimes
print "Nickels: %d" % nickels
print "Pennies: %d" % pennies