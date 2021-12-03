# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 10:56:41 2021

@author: miste
"""

'''
    operatory logiczne:
        and
        or
        not
        in
        is
    powiedzmy ze szczescie poczujemy wtedy kiedy jest:
        weekend
        jest ladna pogoda
        nie mamy nic do roboty
    zacznijmy od zdefiniowania zmiennych ktore okresla wlasnie te rachunki
'''
IsWeekend = True
print("Is weekend =",IsWeekend)

Temperature = 22
print("Temperature =",Temperature)

ToDoList=''
print("ToDoList =",ToDoList)
#teraz wyznacze wartosc zmiennej logicznej wykorzystujac operatory logiczne
IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''
print("IsHappy=",IsHappy)
'''
    == rowna
    > wieksza
    >= wieszka lub rowna
    != nierowna
    
    patrzac na zmienna IsHappy widzimy ze szczescie nasze wynika z tego ze:
        jest weekend i(and) temperatura jest wieksza jak lub rowna(>=) jak
        20 stopni i(and) nie mam nic do roboty
    
    przypuscmy teraz ze temperatura spadla do 5 stopni.
    Poziom szczescia opadnie poniewaz nie spelnia oczekiwan >= 20 stopni lub wiecej
'''
print('-------------------------')
IsWeekend = True
print("Is weekend =",IsWeekend)

Temperature = 5
print("Temperature =",Temperature)

ToDoList=''
print("ToDoList =",ToDoList)
IsHappy = IsWeekend and Temperature >= 20 and ToDoList == ''
print("IsHappy=",IsHappy)
'''
    
    zmienmy teraz warunek szczescia nie zmieniajac zmiennych, 
    powiedzmy ze jestesmy szczesliwy poza weekendem, pogoda jest brzydka a my mamy cos do roboty
    
'''
print('-------------------------')
IsWeekend = True
print("Is weekend =",IsWeekend)

Temperature = 5
print("Temperature =",Temperature)

ToDoList=''
print("ToDoList =",ToDoList)
IsHappy = not IsWeekend and Temperature < 20 and ToDoList != ''
print("IsHappy=",IsHappy)
'''
    (not IsWeekend) oznacza ze jestesmy w normalnym dniu roboczym
    mniej (<) jak 20 stopni
    nie mamy nic do roboty != 
    
    zmienmy teraz nasze warunki wejsciowe:
        nie ma juz weekendu /IsWeekend = False
        i musimy zrobic zakupy/ ToDoList='shopping'
'''
print('-------------------------')
IsWeekend = False
print("Is weekend =",IsWeekend)

Temperature = 5
print("Temperature =",Temperature)

ToDoList='Shopping'
print("ToDoList =",ToDoList)
IsHappy = not IsWeekend and Temperature < 20 and ToDoList != ''
print("IsHappy=",IsHappy)

'''
    jak widac teraz jestesmy szczesliwi
    
    2 warunki mozemy polaczyc w alternatywe i polaczyc je spujnikiem lub (or)
    jezeli kod jest za dlugi i chcesz go kontynuawac w kolejnej linijce
    moge uzyc przcisku backslash (\) i spokojnie kontynuowac
'''
print('-------------------------')
IsWeekend = False
print("Is weekend =",IsWeekend)

Temperature = 5
print("Temperature =",Temperature)

ToDoList='Shopping'
print("ToDoList =",ToDoList)
IsHappy = not IsWeekend and Temperature < 20 and ToDoList != '' \
or IsWeekend and Temperature >= 20 and ToDoList == ''
print("IsHappy=",IsHappy)
'''
    teraz zakladamy ze jestem szczesliwy kiedy:
        jest weekend, jest wiecej jak 20 stopni i nie mamy nic do roboty
        lub (or)
        nie ma weekendu, jest mniej jak 20 stopni i mamy cos do roboty
    
    kiedy zmienimy warunki i powiedzmy:
        nie ma weekendu
        pogoda jest piekna i jest 25 stopni
        mamy cos do zrobienia
'''
print('-------------------------')
IsWeekend = False
print("Is weekend =",IsWeekend)

Temperature = 25
print("Temperature =",Temperature)

ToDoList='Shopping'
print("ToDoList =",ToDoList)
IsHappy = not IsWeekend and Temperature < 20 and ToDoList != '' \
or IsWeekend and Temperature >= 20 and ToDoList == ''
print("IsHappy=",IsHappy)
#jak widac nie jestesmy szczesliwi nawet jezeli zmienie ze jest weekend dalej wyjdzie false bo musimy zrobic zakupy
'''
    trzeba pamietac ze python jest bardzo wrazliwy na wielkosc znakow
    jezeli zrobie chodz jedna literowke taka jak true zamiast True
    kod przestanie dzialac i wyskoczy blad
    tak samo przy Or And itp.
    
    mozna zamieniac zmienne takie jak:
        jezeli chce napisac ze lista nie ma byc pusta moze uzyc
        not ToDoList ==
        wynik bedzie taki sam jakbym uzyl
        ToDoList !=
        liczy sie to rowniez not Temperature >= (<)
        
    mozna robic alternatywy dwoch warunkow, np:
        not (Temperature >= 20 or ToDoList == '')
        wynikiem jest wtedy to:
            kod bierze dwie zmienne i porownuje je ze soba, jezeli jedna z nich
            jest pozytywna do naszych wymogow szczescia to bedziemy szczesliwi
'''
print('-------------------------')
IsWeekend = False
print("Is weekend =",IsWeekend)

Temperature = 25
print("Temperature =",Temperature)

ToDoList='Shopping'
print("ToDoList =",ToDoList)
IsHappy = not IsWeekend and (Temperature < 5 or ToDoList != '')
print("IsHappy=",IsHappy)

































