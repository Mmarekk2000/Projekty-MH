# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 13:13:49 2021

@author: miste
"""

'''
    kiedy pracuje ze zmiennymi wcale nie musze okreslac jakiego typu
    jest dana zmienna. Po prostu przypisuje jej wartosc, a python
    w oparciu o ta wartosc sprobuje dopasowac do zmiennej najelpszy typ
'''
Title = 'Python'
print('Title is',type(Title))

Version = 3
print('Version is',type(Version))

Progress = 0.21
print('Progress is',type(Progress))

'''
    jak widac na tym przykladzie, Title do ktorego przypisalem napis jest
    typu 'str' czyli napis
    Version do ktorego przypisalem cyfre 3 jest typu 'int' czyli liczba calkowita
    oraz Progress do ktorego przypisalem 0.21 jest typu 'float'
    
    podobna logika ma miejsce kiedy wykonuje operacje na zmiennej roznego typu.
    Pewne typy sa silniejsze a pewne typy sa slabsze, i naprzyklad mnazac przez
    siebie zmienna typu int przez zmienna typu float otrzymam wynik ktory
    jest typu float:
'''
print('This expression is',type(Progress * Version))
print('3 * 0.21 = ',(3 * 0.21))
wynik = 0.63
print('0.63 = ',type(wynik))

'''
    od czasu do czasu zdarza sie ze w skrypcie trzeba zainicjowac kilka
    zmiennych ta sama wartoscia, przyklad:
'''
x = 1
y = 1
z = 1

print(x,y,z)

#w pythonie mozna zrobic to inaczej:
a=b=c=2
print(a,b,c)
'''
    w tej chwili a,b i c to po prostu nazwy dla jednego wspolnego miejsca
    w pamieci,a w tym miejscu jest wpisana liczba 2.
    a co jezeli zmienie wartosc jednej ze zmiennych? przekonajmy sie:
'''
c = 3
print(a,b,c)
'''
    nic zlego sie nie stalo, zmienna c wskazuje po prostu w inny obszar pamieci
    w ktorym znajduje sie liczba 3.
    Widac ze 'pythonowe' zapisywanie zmiennych moze troche skrocic moj skrypt
    --------------------------------------------------------------------------
    python tak jakby korzysta z zasad matematycznych, w przykladach obliczen
    takich jak 2+(2+2)*2, python najpierw oblicza () pozniej dzieli i na koncu
    dodaje do siebie liczby.
'''
print(2+(2+2)*2)
print(6/2*(1+2))
#dlaczego wynik jest typem float?
print(4**3**2)
#aby obliczyc potege nalezy wykorzystac **
'''
    sposob na zmiane zmiennych wartosci liczbowych
'''
x=1
print(x+1)
print(x)
x=x+1
print(x)
#to nie jedyny sposob na zmiane wartosci
x+=1
print(x)
#ten zapis jest po prostu troche krotszy a za tym idzie ze jest wygodniejszy
x-=1
print(x)
