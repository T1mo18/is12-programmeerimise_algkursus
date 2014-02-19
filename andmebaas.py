#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

joogid= [
['6lu', 'Heineken', '0.3'],
['Vein', 'Old Tbilisi', '1.0'],
['Viin', 'Viru Valge', '1.0'],
['Viski', 'Jack Daniels', '0.7'],
['Konjak', 'Martell', '0.7'],
]

x=len(joogid)

def list():
		print joogid
	
def remove():
		print joogid
		joogid.pop(int(raw_input("sisestage number 0-..., et mõni automark eemaldada: ")))
		print joogid

def append():
		joogid.insert(x,[raw_input("Sisestage jook: "), raw_input("Sisestage joogi mark: "), raw_input("Sisestage pudeli suurus: ")]) 
		print joogid

def quit():
		sys.exit(0)


while True:
		print " "
		print "append-Andmebaasi kirje lisamine"
		print "remove-Andmebaasist kirje eemaldamine "
		print "list-Andmebaas"
		print "quit-Andmebaasist väljumine"
		print " "
		
		sisestus= raw_input("valige endale sobiv varjant: ")
		
		if sisestus=="append":
			append()
		elif sisestus=="remove":
			remove()
		elif sisestus=="list":
			list()
		elif sisestus=="quit":
			quit()
		else: 
			print "Vale sisestus, proovige uuesti!"
			
