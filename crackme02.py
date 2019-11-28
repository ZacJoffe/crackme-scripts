#!/usr/bin/env python3

pssw = "password1"

new_pass = ""

for p in pssw:
    new_pass += chr(ord(p) - 1)
print(new_pass)

