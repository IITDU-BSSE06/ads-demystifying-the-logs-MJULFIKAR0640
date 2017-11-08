#!/usr/bin/python

import sys

count2009=0
count2010=0
count2011=0

for line in sys.stdin:
	data = line.strip()

	if "2009" in data:
 		count2009+=1
	else if "2010" in data:
 		count2010+=1
	if "2011" in data:
 		count2011+=1

print "2009", "  ", count2009
print "2010", "  ", count2010
print "2011", "  ", count2011
