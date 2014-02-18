#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys



print "add- lisab andmebaasi masiivi"
print "rm- eemaldab masiivist teatud rea"
print "ls- kuvatakse andmebaas"
print "q- lahkuge andmebaasist"
print " "
sisestus= raw_input("valige endale sobiv varjant: ")


joogid= [


['Õlu', 'Heineken', '0.3'],
['Vein', 'Old Tbilisi', '1.0'],
['Viin', 'Viru Valge', '1.0'],
['Viski', 'Jack Daniels', '0.7'],
['Konjak', 'Martell', '0.7'],
]

x=len(joogid)


def add():
	if sisestus=='add':
		joogid.insert(x,[raw_input("Sisestage jook: "), raw_input("Sisestage joogi mark: "), raw_input("Sisestage pudeli suurus: ")]) 

add()

def rm():
	if sisestus=='rm':
		print joogid
		joogid.pop(int(raw_input("sisestage number 0-..., et mõni automark eemaldada: ")))
rm()

def ls():
	if sisestus=='ls':
		print joogid
ls()		

def quit():
	if sisestus=='q':
		sys.exit(0)
quit()
