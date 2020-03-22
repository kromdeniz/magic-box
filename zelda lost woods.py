# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:08:36 2020

@author: mnm
"""

####################
## EXAMPLE: while loops 
## Try expanding this code to show a sad face if you go right
## twice and flip the table any more times than that. 
## Hint: use a counter
####################
#n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
#while n == "right" or n == "Right":
#    n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
#print("\nYou got out of the Lost Forest!\n\o/")

n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
if n == "right" or n == "Right":
 n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
if n == "right" or n == "Right":
 n = input("You are in the Lost Forest\n****************\n****************\n :((\n****************\n****************\nGo left or right? ")
while n == "right" or n == "Right":
     n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ") 
print("\nYou got out of the Lost Forest!\n\o/")    