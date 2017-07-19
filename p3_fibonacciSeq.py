# Fibonacci Sequence
# Enter a number and have the program generate the Fibonacci sequence to that Nth number.

a = 0
b = 1
while True:
    try:
        num = int(raw_input("How many numbers of Fibonacci? "))
        if num in range(0,1000):
            print "\nFIBONACCI NUMBERS:"
            for i in range(0,num):
                print a
                x = a + b
                a = b
                b = x
            break
        else:
            print "Please enter a positive whole number that is less than 1000."
    except:
        print "Please enter a positive whole number that is less than 1000."
