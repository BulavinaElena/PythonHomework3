#<Задание 2>
#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16]
#[2, 3, 5, 6] => [12, 15]

from random import randint as rI
numbers=int(input('Введите размер списка: '))
firstList=[]
for i in range(numbers):
    firstList.append(rI(-15, 15))
print(firstList)
listLenght=len(firstList)
resultList=[]
for i in range(listLenght//2+1):
    element=firstList[i]*firstList[listLenght-i-1]
    resultList.append(element)
print(resultList)
