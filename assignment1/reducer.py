#!/usr/bin/python

import sys

count=0

for line in sys.stdin:
	data = line.strip().split("\t")
	
	hitIP= str(data[0])
	if "10.99.99.186" == hitIP:
		countTotal+=1


print count
