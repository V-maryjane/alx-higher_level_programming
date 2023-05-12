#!/usr/bin/python

for a in range(100):
    if a < 99:
        print("{:02d}".format(a), end=', ')
    else:
        print(a)
