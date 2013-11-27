#!/usr/bin/env python
# -*- coding: utf8 -*-

########################ÜL2############################################

print "Esimene nr. peab olema väiksem kui teine!"
number1 = int(raw_input("Sisesta esimene number: "))
number2 = int(raw_input("Sisesta teine number: "))
jagub = 3
def arvud(number1, number2, jagub):
	if number1 > number2:	
		number1,number2 = number2,number1	
		number1 = number1 + (jagub -(number1 % jagub))
		return [i for i in range(number1, number2, jagub)]

vastus = [i for i in range((number1 + (jagub - (number1 % jagub))),number2,jagub)]
print "Numbrite vahel on " + str(len(vastus)) + " numbrit, mis jaguvad 3-ga"


########################ÜL1############################################

tekst = raw_input("Sisesta tekst: ")

if tekst == str(tekst.lower()) and any(c.isdigit() for c in tekst):
	print "V2iksed t2hed ja numbrid"
elif tekst == str(tekst.upper()) and any(c.isdigit() for c in tekst):
	print "Suured t2hed ja numbrid" 




elif tekst == str(tekst.lower()):
	print "V2iksed t2hed ja numbriteta"
elif tekst == str(tekst.upper()):
	print "Suured t2hed ja numbriteta"




elif any(c.isdigit() for c in tekst):
	print "Suured t2hed/V2iksed t2hed ja numbrid"
else:
	print "Suured t2hed/V2iksed t2hed ja numbriteta"
