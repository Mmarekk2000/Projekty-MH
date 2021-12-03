# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:11:53 2021

@author: miste
"""

name = 'Marek'
age = 21
daysInYear = 365
message = '%s is %d years old, so is about %d days old'
print(message % (name,age,age*daysInYear))
name = 'Kuba'
age = 32
print(message % (name,age,age*daysInYear))
message = '{0:s} is {1:d} years old, so is about {2:d} days old'
print(message.format('Chris',17,17*365))
print('1234567890 divided by 12345 is ',1234567890 // 12345,'and the rest is',1234567890 % 12345)