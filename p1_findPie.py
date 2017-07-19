# FindPie
# This program gives Pi to the indicated decimal place. Maximum = 11.
import math


pi = math.pi
print pi

while True:
    try:
        x = int(raw_input("Pi to how many places? "))
        if x in range(0, 12):
            print "{:.{precision}f}".format(pi, precision=x)
            break
        else:
            print "Number is too high. Maximum precision is 11."
    except:
        print "Try again."
