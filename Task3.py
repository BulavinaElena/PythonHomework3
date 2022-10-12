# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов. 
# Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform as uI
from random import randint as rI
from decimal import Decimal
numbers=int(input('Введите размер списка: '))
firstList=[]
for i in range(numbers):
    pos=rI(1, 4)
    numbers=Decimal(f'{round(uI(0, 10), pos)}')
    firstList.append(numbers)
secondList=[]
mantissa=[]
for n in firstList:
    secondList.append(float(n))
    if abs(n)-int(abs(n)) !=0.0:
        mantissa.append(abs(n)-abs(int(n)))
print(secondList)
print(f'Максимальная {max(mantissa)} и минимальная {min(mantissa)} мантиссы')
print(f'Разница мантисс = {max(mantissa)-min(mantissa)}')


list1=[1.1, 1.2, 3.1, 5, 10.01]
