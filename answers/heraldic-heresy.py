#Problem        : Heraldic Heresy
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

def check_line(line):
    metal = 0
    color = 0
    met = ''
    col = ''

    charCount = 0
    for character in list(line):
        if character.isupper():
            if charCount > 0 and met != '' and metal > 0 and met != character:
                print("INVALID")
                sys.exit()
            met = character
            metal = metal + 1
            if color > 0:
                color = color - 1
        else:
            if charCount > 0 and col != '' and color > 0 and col != character:
                print("INVALID")
                sys.exit()
            col = character
            color = color + 1
            if metal > 0:
                metal = metal - 1

        charCount = charCount + 1

data = sys.stdin.read().splitlines()

N = int(data[0].split()[0])
M = int(data[0].split()[1])

# horizontal
for line in data[1:N + 1]:
    check_line(line)

# vertical
index = 0

for i in range(len(data[0]) - 1):
    l = ''
    for line in data[1:N + 1]:
        l = l + line[i]
    check_line(l)



print ("VALID")
