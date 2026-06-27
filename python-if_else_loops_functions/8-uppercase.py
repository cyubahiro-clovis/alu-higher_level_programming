#!/usr/bin/python3


def uppercase(str):
    for c in str:
        n = ord(c)
        print("{}".format(chr(n - 32) if 97 <= n <= 122 else c), end="")
    print("")
