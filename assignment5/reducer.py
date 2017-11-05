#!/usr/bin/python

import sys
from urlparse import urlparse

path_dictonary = {}

for line in sys.stdin:
	data = line.strip().split("\t")
	
	path = data[0]
    	url = urlparse(path).path
     
    	if not url in path_dictonary:
        	path_dictonary[url] = 1
    	else:
        	path_dictonary[url] += 1
       

print len(path_dictionary)
