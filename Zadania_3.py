import sys
#Zadanie_1
#a = [1-x for x in range(1,11)]
#print(a)
#b = [4**n for n in range(0, 8)]
#print(b)
#c = [x for x in b if x%2!=1]
#print(c)

#Zadanie_2
#import random
#lista1 = random.sample(range(1, 101), 10)
#print(lista1)
#lista2 = [x for x in lista1 if x%2==0]
#print(lista2)

#Zadanie_3
#lista = {'majonez':'słoik', 'jajka':'sztuk', 'chleb':'sztuk', 'mleko':'butelek', 'ziemniaki':'kg'}
#nowalista = {}
#for klucz, wartosc in lista.items():
#    if wartosc == 'kg':
#        nowalista[wartosc]=klucz
#print(nowalista)

#Zadanie_4
#def trojkat(a, b, c):
#    if c**2 == a**2 + b**2 or b**2 == a**2 + c**2 or a**2 == b**2 + c**2:
#        print("Trójkąt jest prostokątny")
#    else:
#        print("Trójkąt nie jest prostokątny")
#a = int(input("Podaj 1 bok: "))
#b = int(input("Podaj 2 bok: "))
#c = int(input("Podaj 3 bok: "))
#print(trojkat(a, b, c))

#Zadanie_5
#def trapez(a, b, h):
#    pole = ((a+b)*h/2)
#    return(pole)
#print(trapez(10, 16, 7))

#Zadanie_6_i_7
#def funkcja(a1, b, ile):
#    for x in range (1, ile+1):
#        print(a1*(b**(x-1)))
#funkcja(1, 4, 10)