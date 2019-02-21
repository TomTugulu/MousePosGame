# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 13:57:26 2019
@author: tuguluth
"""

# 

#Import Packages
import pyautogui
from random import randint
from time import sleep

#Set Score
score = 0

#Set first target
o = randint(1,2559)
p = randint(1,1022)

#Alert user to exit, print first target
print('Press Ctrl-C to quit.')
print("Target = X: ", o, ", Y: ", p )


try:
    while True:
        
       #Get and print the mouse coordinates.
       x, y = pyautogui.position()
       positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
       print(positionStr, end='')
       print('\b' * len(positionStr), end='', flush=True)
       
       # Checks for hits
       if x == o and y == p:
           print("~~~~~~~~~~~~~~~~~~~~Hit~~~~~~~~~~~~~~~~~~~~")
           #Resets target
           o = randint(1,2559)
           p = randint(1,1022)
           sleep(0.5)
           score += 1
           
           #Checks if target score hit
           if score == 5:
               print('\nWinner!')
               break
           
           #If not hit, give new target zone
           else:
               print("\nSCORE: ",score)
               print("\nNew Target = X: ", o, ", Y: ", p )

#If Exit key hit, break the loop and end    
except KeyboardInterrupt:
    print('\nGame Quit.')