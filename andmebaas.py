#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

print "append-Andmebaasi kirje lisamine"
print "remove-Andmebaasist kirje eemaldamine "
print "list-Andmebaas"
print "quit-Andmebaasist väljumine"
print " "
sisestus= raw_input("valige endale sobiv varjant: ")


joogid= [
['6lu', 'Heineken', '0.3'],
['Vein', 'Old Tbilisi', '1.0'],
['Viin', 'Viru Valge', '1.0'],
['Viski', 'Jack Daniels', '0.7'],
['Konjak', 'Martell', '0.7'],
]

x=len(joogid)

def list():
	if sisestus=='list':


		print joogid
list()	



def remove():
	if sisestus=='remove':
		print joogid
		joogid.pop(int(raw_input("sisestage number 0-..., et mõni automark eemaldada: ")))
remove()

	

def append():
	if sisestus=='append':
		joogid.insert(x,[raw_input("Sisestage jook: "), raw_input("Sisestage joogi mark: "), raw_input("Sisestage pudeli suurus: ")]) 
append()



def quit():
	if sisestus=='quit':
		sys.exit(0)
quit()
