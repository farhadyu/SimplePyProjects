# NEXT PRIME
# By: Farhad Yusifov, 15/07/2017

# This program finds the next prime number. You can start at any number.
from math import sqrt


def next_prime(num):
    num = num + 1
    while True:
        for i in xrange(1, int(sqrt(num))+1):  # Find a factor of num
            if num % i == 0 and i > 1:  # If factor exists
                num += 1
                break
            elif i == int(sqrt(num)):  # If no factor exists
                return num


def main():
    num = int(raw_input("Starting number: "))
    num = next_prime(num)
    while True:
        print "Prime:", num
        proceed = raw_input("Next prime [y/n]? ")

        if proceed.upper() == "Y":
            num = next_prime(num)   # Run the function to find the next prime

        else:
            print "DONE"
            break

main()
