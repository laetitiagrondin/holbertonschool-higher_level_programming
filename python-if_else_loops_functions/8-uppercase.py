#!/usr/bin/env python3
def uppercase(str):
    for i in range(len(str)):
        c = str[i]
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print()
