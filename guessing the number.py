# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 09:44:43 2019

@author: cousi
"""

import random


def guess(number):
    num = random.randint(1,100)
    print(num)
    if num==number:
        print("You guess the right number. YOU WIN!!!!!!!!")
    elif num >= number:
        print("You guess smaller number.OOPS YOU LOSE!!!!!!!!!!!")
    else :
        print("You guess the bigger number.OOPS YOU LOSE!!!!!!!!!!!!!!!!!!!")
        
number = int(input("Please guess the number at range 1 - 100: "))
if number>=101:
    print("Number is too big please enter the smaller number.")
    number = int(input("Please guess the number at range 1 - 100: "))
elif number<=0:
    print("You entered too small number like your dick. So please enter big number.")
guess(number)










