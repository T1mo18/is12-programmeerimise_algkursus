#!/usr/bin/env python
# -*- coding: utf-8 -*-


def ruut(h,w):
		
		x=0
		while x < w:
			x = x + 1
			
			y = 0
			while y < h:
				print "@",
				y = y + 1
			print ""


print ruut(10,10)
