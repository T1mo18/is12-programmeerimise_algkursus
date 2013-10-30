#!/usr/bin/env python
# -*- coding: utf-8 -*-
def keskmine():
    esimene=(raw_input("Sisesta esimene arv: "))
    if esimene=="":
        print "Ei sisestatud esimest arvu"
        return keskmine()
    teine=int(raw_input("Sisesta teine arv: "))
    if teine=="":
        print "Ei sisestatud teist arvu"
        return keskmine()
    summa = float(int(esimene)+int(teine))
    b=float(int(summa)/2.0)
    print ("Nende arvude keskmine on "+str(b))

    print "___________________________________________________________________"




def fjada():
    arv=input("Sisesta üks number, peale mida kuvatakse fibonacci jada:")
    esimene, teine = 0, 1
    while esimene<arv:
        print esimene,
        esimene, teine = teine, esimene+teine


    print "____________________________________________________________________"   

def ruutfunktsioon():
    print "Ruutfunktsioon \nax(ruut)+bx+c=0\nAnna väärtused a-le, b-le ja c-le\n Teile kuvatakse ruutfunktsioon koos vastustega"
    print"______________________________________________________________________"
    a=raw_input("Sisesta a väärtus, arvu ette kas +või-:")
    b=raw_input("Sisesta b väärtus, arvu ette kas +või-:")
    c=raw_input("Sisesta c väärtus, arvu ette kas +või-:")
    print"______________________________________________________________________"
    print 'Te sisestasite ruutfunktsiooni mis näeb välja nii, ' +a+'x(ruut)'+b+'x'+c+'=0'
    juur=((int(b)*int(b))-4*(int(a)*int(c)))
    ac=(4*(int(a)*int(c)))
    b2=((int(b)*int(b)))
    aa=(int(a)*2)
    if int(juur)<int(ac):
        print "Ruutfunktsioonil puuduvad lahendid, kuna juur ei lahene!"
    else:
        ruutjuur=int(juur)**.5
        x1=(-(float(b))-int(ruutjuur))
        x2=(-(int(b))+int(ruutjuur))
        x1=round(float(x1)/float(aa),2)
        x2=round(float(x2)/float(aa),2)
        print "Ruutfunktsiooni lahendid on:"+str(x1)+" ja "+str(x2)


fjada()
ruutfunktsioon()
keskmine()
