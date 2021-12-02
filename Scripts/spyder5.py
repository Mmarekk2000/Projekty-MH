# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 13:37:11 2021

@author: miste
"""

helloMessage= "Hello %s!"
print(helloMessage % ('Kate'))
print(helloMessage % ('Chris'))
helloMessage2 = "Hello {0:s}!"
print(helloMessage2.format('Kate'))
print(helloMessage2.format('Chris'))
helloMessage3 = "%s has %d %s"
print(helloMessage3 % ("Kate",1,"animal"))
print(helloMessage3 % ("Chris",100000,"$"))
helloMessage4 = "{0:s} has {1:d} {2:s}"
print(helloMessage4.format('Kate',1,'animal'))
print(helloMessage4.format('Chris',100000,'$'))
line = '{0:20s} costs {1:6d} €'
print(line.format('ICE CREAM',3))
print(line.format('TRIP TO VENICE',119))
print(line.format('PIZZA HAWAII',6))
line = '{0:s} {1:d}'
print(line.format('ICE CREAM', 3))
print(line.format('TRIP TO VENICE', 119))
print(line.format('PIZZA HAWAII', 6))