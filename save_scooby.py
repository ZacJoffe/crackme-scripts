#!/usr/bin/env python3

import os
cwd = os.getcwd()

# cwd = cwd.replace("/", "$")

newStr = ""

for char in cwd:
    if char == "/":
        char = "$"
    else:
        if ord(char) < ord('a') or ord('z') < ord(char):
            if ord('@') < ord(char) and ord(char) < ord('['):
                char = chr(ord(char) + 30)
                # chr(ord('a')+1)
        else:
            char = chr(ord(char) - 30)
    newStr += char

print(newStr)
