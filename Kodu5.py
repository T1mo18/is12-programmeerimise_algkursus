from random import randint


kuulid = ["s"]*5 + ["m"]*10 + ["v"]*15


arv=len (kuulid)-1
print arv
kuul= randint(0,arv)
print kuul
kuul1=kuulid[kuul]
print kuul1
del kuulid [kuul]




arv=len (kuulid)-1
print arv
kuul= randint(0,arv)
print kuul
kuul2=kuulid[kuul]
print kuul2
del kuulid [kuul]

print "________________________________________________________"

from random import randint
import time

klass = ['Art','Janis','Sander','Egert','Margen','Marek','Kerto','Eveli','Jasper','Mario','Kairo','Ardo',
'Riigo','Janar','Katerin','Rait','Aulis','Mariin','Timo','Aleks','Aigar','Arti']

print klass


print len (klass)

a=len(klass)

min= 0
max= a-1

a = randint (min,max)

print klass [a]

print "--------------------------------------"
print klass [randint(0,len(klass)-1)]










