#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if char != ord('q') and char != ord('e'):
        print(chr(char), end="")
