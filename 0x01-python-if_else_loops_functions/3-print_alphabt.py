#!/usr/bin/python3
# Author Maryjane
for char in range(97, 123):
    if char not in (113, 101):
        print("{}".format(chr(char)), end='')
