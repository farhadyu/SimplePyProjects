# FindE
# This program gives e to the indicated decimal place. Maximum = 11.
from math import e


print e

while True:
    try:
        x = int(raw_input("Pi to how many places? "))
        if x in range(0, 12):
            print "{:.{precision}f}".format(e, precision=x)
            break
        else:
            print "Number is too high. Max is 11."
    except:
        print "Try again."
