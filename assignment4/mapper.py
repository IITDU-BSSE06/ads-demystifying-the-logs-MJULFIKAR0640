#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("GET")
    if (len(data) >1):
        hitaddress = data[1]
        print hitaddress
