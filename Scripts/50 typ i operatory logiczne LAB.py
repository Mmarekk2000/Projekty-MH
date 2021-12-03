# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:57:50 2021

@author: miste
"""

isAutomaticMode = True
print("Automatic mode:   ",isAutomaticMode)
is80PercentLight = True
print("Is the light good:",is80PercentLight)
isDirectLight = False
print("Is sun low:       ",isDirectLight)
isRainy= False
print("Is it rainy:      ",isRainy)
turnLightsOn = isAutomaticMode and is80PercentLight == False and (isDirectLight or isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('----------------------------------------------------------')

isAutomaticMode = True
print("Automatic mode:   ",isAutomaticMode)
is80PercentLight = False
print("Is the light good:",is80PercentLight)
isDirectLight = False
print("Is sun low:       ",isDirectLight)
isRainy= False
print("Is it rainy:      ",isRainy)
turnLightsOn = isAutomaticMode and (is80PercentLight or isDirectLight or isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('----------------------------------------------------------')

isAutomaticMode = True
print("Automatic mode:   ",isAutomaticMode)
is80PercentLight = True
print("Is the light good:",is80PercentLight)
isDirectLight = False
print("Is sun low:       ",isDirectLight)
isRainy= True
print("Is it rainy:      ",isRainy)
turnLightsOn = isAutomaticMode and (is80PercentLight or isDirectLight or isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('----------------------------------------------------------')

isAutomaticMode = True
print("Automatic mode:   ",isAutomaticMode)
is80PercentLight = True
print("Is the light good:",is80PercentLight)
isDirectLight = True
print("Is sun low:       ",isDirectLight)
isRainy= False
print("Is it rainy:      ",isRainy)
turnLightsOn = isAutomaticMode and (is80PercentLight or isDirectLight or isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('----------------------------------------------------------')

isAutomaticMode = True
print("Automatic mode:   ",isAutomaticMode)
is80PercentLight = False
print("Is the light good:",is80PercentLight)
isDirectLight = False
print("Is sun low:       ",isDirectLight)
isRainy= True
print("Is it rainy:      ",isRainy)
turnLightsOn = isAutomaticMode and (is80PercentLight or isDirectLight or isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('----------------------------------------------------------')

isAutomaticMode = False
print("Automatic mode:   ",isAutomaticMode)
is80PercentLight = True
print("Is the light good:",is80PercentLight)
isDirectLight = False
print("Is sun low:       ",isDirectLight)
isRainy= True
print("Is it rainy:      ",isRainy)
turnLightsOn = isAutomaticMode and (is80PercentLight or isDirectLight or isRainy)
print("TURN LIGHTS ON:   ",turnLightsOn)
print('----------------------------------------------------------')