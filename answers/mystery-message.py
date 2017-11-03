#Problem        : Mystery Message
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys, string

data = sys.stdin.read().splitlines()

for line in data:

    words = line.split()
    word = words[0].lower()
    cipher = ord(words.pop().lower()[0])

    print ((ord(word[0]) - cipher) % 26)
