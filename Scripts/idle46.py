Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/miste/source/repos/RatujLudzi/ratuj-ludzi/Scripts/idle46.py

= RESTART: C:/Users/miste/source/repos/RatujLudzi/ratuj-ludzi/Scripts/idle46.py
8*3
24
five = 5
three = 3
five * three
15
'''
    mozna pytac sie o typy zmiennych taki jak 5 czy five, mozna rowniez pytac
    sie o typy zmiennych wyniku dzialania, przyklad:
'''
'\n    mozna pytac sie o typy zmiennych taki jak 5 czy five, mozna rowniez pytac\n    sie o typy zmiennych wyniku dzialania, przyklad:\n'

type(five)
<class 'int'>
type(5)
<class 'int'>
type(five*three)
<class 'int'>
'''
    typ int opisuje wlasnie liczby calkowite. Niewazne czy te liczby sa dodatnie
    czy ujemne. Dopoki jest liczba calkowita, jest typem int
'''
'\n    typ int opisuje wlasnie liczby calkowite. Niewazne czy te liczby sa dodatnie\n    czy ujemne. Dopoki jest liczba calkowita, jest typem int\n'
'''
    typ int opisuje wlasnie liczby calkowite. Niewazne czy te liczby sa dodatnie
    czy ujemne. Dopoki jest liczba calkowita, jest typem int.
    Dla odroznienia mozna spotkac sie z liczbami ktore nie sa liczbami
    calkowitymi, aby zobaczyc taka liczbe podaje przyklad:
'''
'\n    typ int opisuje wlasnie liczby calkowite. Niewazne czy te liczby sa dodatnie\n    czy ujemne. Dopoki jest liczba calkowita, jest typem int.\n    Dla odroznienia mozna spotkac sie z liczbami ktore nie sa liczbami\n    calkowitymi, aby zobaczyc taka liczbe podaje przyklad:\n'
five/three
1.6666666666666667
#jak widac python nie ma problemu z obliczeniem takiej liczby, ale jak nazywa sie ten typ?
type(five/three)
<class 'float'>
'''
    typ float jest dosc precyzyjny, patrzac na to ile jest miejsc po przecinku
    do tego aby wyznaczyc wartosc 2/3. Jednak typ float slynie z tego ze wkoncu
    musi gdzies zaokraglic liczbe. Dlatego nie jest w 100% dokladny.
    W matematyce jest to dokladnie 1 i 2/3 lecz float musi gdzies to zaokraglic,
    jest to daleko, blad nie jest wielki, ale nie jest to typ precyzyjny.
'''
'\n    typ float jest dosc precyzyjny, patrzac na to ile jest miejsc po przecinku\n    do tego aby wyznaczyc wartosc 2/3. Jednak typ float slynie z tego ze wkoncu\n    musi gdzies zaokraglic liczbe. Dlatego nie jest w 100% dokladny.\n    W matematyce jest to dokladnie 1 i 2/3 lecz float musi gdzies to zaokraglic,\n    jest to daleko, blad nie jest wielki, ale nie jest to typ precyzyjny.\n'
# jak duze wartosci mozna wprowadzac w pythonie?
import sys
sys.maxsize
9223372036854775807
'''
    sys to specjalny modul, w ktorym mozesz odnalesc stala sys.maxsize ktora
    okresla jak duze wartosci liczbowe mozna zapisac w postaci liczby int.
    Jesli jednak dokladniej wczytac sie w dokumentacje pythona, okaze sie ze mozemy
    definiowac o wiele wieksze wartosci, ktore nadal beda rozpoznazywane jako
    wartosci int. Przyklad:
'''
'\n    sys to specjalny modul, w ktorym mozesz odnalesc stala sys.maxsize ktora\n    okresla jak duze wartosci liczbowe mozna zapisac w postaci liczby int.\n    Jesli jednak dokladniej wczytac sie w dokumentacje pythona, okaze sie ze mozemy\n    definiowac o wiele wieksze wartosci, ktore nadal beda rozpoznazywane jako\n    wartosci int. Przyklad:\n'
veryBigValue = 9999999999999999999999999999999999999999999999999999999
veryBigValue
9999999999999999999999999999999999999999999999999999999
#mozna zobaczyc ze wartosc zostala zapamietana
veryBigValue + 1
10000000000000000000000000000000000000000000000000000000
'''
    mozemy zobaczyc ze wartosc zostala zapamietana. mozna rowniez wykonywac
    na niej dzialania, jednak dalej zostaje typem int.
'''
'\n    mozemy zobaczyc ze wartosc zostala zapamietana. mozna rowniez wykonywac\n    na niej dzialania, jednak dalej zostaje typem int.\n'
type(veryBigValue)
<class 'int'>
(veryBigValue+1)/2
5e+54
#pomimo ze jest to dalej liczba calkowita, zostala ona zaprezentowana
#w postaci liczby float
type(veryBigValue+1)/2
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    type(veryBigValue+1)/2
TypeError: unsupported operand type(s) for /: 'type' and 'int'
type(veryBigValue+1)/2
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    type(veryBigValue+1)/2
TypeError: unsupported operand type(s) for /: 'type' and 'int'
type((veryBigValue+1)/2)
<class 'float'>

'''
    wartosc zostala przyblizona, nie jest to dokladna wartosc ktorej moglismy sie
    spodziewac po pythonie. Jednakk jezeli jestes w sytuacji ze chcesz aby
    wynik dzialania byl liczba calkowita to mozna sie poslozyc innym przykladem dzielenia.
'''
'\n    wartosc zostala przyblizona, nie jest to dokladna wartosc ktorej moglismy sie\n    spodziewac po pythonie. Jednakk jezeli jestes w sytuacji ze chcesz aby\n    wynik dzialania byl liczba calkowita to mozna sie poslozyc innym przykladem dzielenia.\n'
five//three
1
'''
    dwa // przedstawiaja dzielenie calkowite. Wynik to ilosc trojek ktore mieszcza sie w 5.
    Oczywiscie zostala jakas reszta ktora w tym przypadku to 2. aby dowiedziec sie jaka reszta
    zostala, mozna posluzyc sie dzieleniem modulo. Dzielenie modulo wykonuje sie w pythonie
    przy uzyciu znaku %
'''
'\n    dwa // przedstawiaja dzielenie calkowite. Wynik to ilosc trojek ktore mieszcza sie w 5.\n    Oczywiscie zostala jakas reszta ktora w tym przypadku to 2. aby dowiedziec sie jaka reszta\n    zostala, mozna posluzyc sie dzieleniem modulo. Dzielenie modulo wykonuje sie w pythonie\n    przy uzyciu znaku %\n'
five % three
2
'''
    w matematyce wystepuje jeszcze nieskonczonosc ale jak wiemy zaden z komputerow nie zna
    czegos takiego. Lecz python potrafi cos takiego obsluzyc. Aby zobaczyc czym dla pythona
    jest nieskonczonosc zrzutuj na typ float, przyklad:
'''
'\n    w matematyce wystepuje jeszcze nieskonczonosc ale jak wiemy zaden z komputerow nie zna\n    czegos takiego. Lecz python potrafi cos takiego obsluzyc. Aby zobaczyc czym dla pythona\n    jest nieskonczonosc zrzutuj na typ float, przyklad:\n'
float('inf')
inf
#jest to operacja rzutowania z ktora juz mialem stycznosc przy napisach ktore zawieraly w sobie same cyfry wiec mogly byc zamienione na liczbe.
#int = infinity
float('inf') > 9999999999999999999999999
True
float('inf') > 999999999999999999999999999999999999999999999999999999
True
float('inf') > 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
True
#pyython zna pojecie nieskonczonosci, jaka liczbe bym nie podal zawsze bedzie ona mniejsza od inf
#pyython zna rowniez pojecie -nieskonczonosci
-float('inf')
-inf
