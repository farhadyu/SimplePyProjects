# PRIME FACTORIZATOR
# By: Farhad Yusifov, 2017/07/14
# Factors the number that is given, and returns a list of its prime factors
from math import sqrt
import time

def factorize(factors):
    while True:
        for i in xrange(1, int(sqrt(factors[-1])) + 1):
            if i % 1000000 == 0:
                a = 100*(float(i/(sqrt(factors[-1]))))
                print "Working... %.1f%%" % a
            if factors[-1] % i == 0 and i != 1:
                last = factors.pop()
                last = last / i
                factors.append(i)
                factors.append(last)
                factors.sort()
                print "progress: ", factors
                break
            elif i == int(sqrt(factors[-1])):
                return factors


def main():
    while True:
        x = int(raw_input("ENTER A POSITIVE INTEGER: "))
        tic = time.clock()
        if x == 1:
            print "\nFACTORS: ", [1]
            break
        elif x > 1:
            factors = [x]
            factors = factorize(factors)
            print "\nFACTORS: ", factors
            break
        else:
            print "ENTER ANOTHER NUMBER"
    toc = time.clock()
    print toc - tic

main()
