# PRIME FACTORIZATOR
# By: Farhad Yusifov, 2017/07/14
# Factors the number that is given, and returns a list of its prime factors
from math import sqrt
import time


def factorize(factors):
    while True:
        if factors[-1] == 2:
            return factors
        # If number is even and larger than 2
        elif factors[-1] % 2 == 0:
            last = factors.pop()
            last = last / 2
            factors.append(2)
            factors.append(last)
            factors.sort()
            print "progress: ", factors
        # Else number is odd
        else:
            for i in xrange(3, int(sqrt(factors[-1])) + 1, 2):
                # Indicates the program is running through large numbers
                if i % 1594323 == 0:
                    a = 100*(float(i/(sqrt(factors[-1]))))
                    print "Working... %.1f%%" % a
                if factors[-1] % i == 0:
                    last = factors.pop()
                    last = last / i
                    factors.append(i)
                    factors.append(last)
                    factors.sort()
                    print "progress: ", factors
                    break
                elif i == int(sqrt(factors[-1])) and i % 2 != 0:
                    return factors
                elif i == int(sqrt(factors[-1])) - 1 and i % 2 != 0:
                    return factors


def main():
    while True:
        x = int(raw_input("ENTER A POSITIVE INTEGER: "))
        tic = time.clock()
        if x in [1, 2, 3]:
            print "\nFACTORS: ", [x]
            break
        elif x > 3:
            factors = [x]
            factors = factorize(factors)
            print "\nFACTORS: ", factors
            break
        else:
            print "ENTER ANOTHER NUMBER"
    toc = time.clock()
    print toc - tic

main()
