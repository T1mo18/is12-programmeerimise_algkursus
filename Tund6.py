from random import randint

klass = ['a', 'b', 'c', 'd' ]

print klass 

n=2

element=klass[n]
del klass [n]

klass=  klass+ [element]
print klass

print"---------------------------------------------"
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
