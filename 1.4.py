# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 16:20:17 2021

@author: Ilona

Пользователь вводит целое положительное число. Найдите самую большую 
цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

print("Введите целое положительное число")
num = input()

if len(num) == 1 :
    print("Наибольшая цифра в числе:", num)
else: 
    pow = len(num)-1
    num = int(num)
    digit = num//10**pow
    num -= digit*10**pow
    newdig = num//10**(pow-1)
    while num > 0: 
        if newdig > digit:
            digit = newdig 
        pow -= 1
        num -= newdig*10**(pow)
        newdig = num//10**(pow-1)
    print("Наибольшая цифра в числе:", digit)