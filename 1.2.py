# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:43:28 2021

@author: Ilona

Пользователь вводит время в секундах. 
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. 
Используйте форматирование строк.
"""

print('Введите время в секундах')
time = int(input())
hours = time//3600
time -= hours*3600
mins = time//60
time -= mins*60
print('{:02d}:{:02d}:{:02d}'.format(hours, mins, time))