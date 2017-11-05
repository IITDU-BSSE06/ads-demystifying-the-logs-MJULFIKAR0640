#!/usr/bin/python

import sys

count=0

for line in sys.stdin:
	data = line.strip().split("\t")
	
	hitaddress= str(data[0])
	if "/assets/js/the-associates.js" in hitaddress:
		countTotal+=1


print count
