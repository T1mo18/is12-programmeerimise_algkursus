#!/usr/bin/env python
# -*- coding: utf8 -*-

q = 1
while q<6:
	
	w=0
	while w<q:
		print "$",
		w=w+1
		
	w=6
	while q<w:
		print "#",
		w=w-1
		
	print ""
	q=q+1
