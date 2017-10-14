#Problem        : Verifying Validity
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()


for line in data:
    thesum = 0
    weight = 3
    if len(line) != 13:
        continue

    for char in list(line):

        # Alternative to for look
        # weight += 2
        # weight %= 4

        if weight == 3:
            weight = 1
        else:
            weight = 3

        # print (weight)
        thesum = thesum + (int(char) * weight)

    # print (thesum)
    if thesum % 10 == 0:
        print("VALID")
    else:
        print("NOT VALID")
