# Задача 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

#Пример:
#для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

number=int(input('Введите предел последовательности Фибоначчи: '))
def Fibona44i(number):
    myList=[1, 0, 1]
    for i in range (2, number+1):
        myList.append(myList[i-1] + myList[i])
    for i in range (0, -number+1, -1):
        myList.insert(0, myList[1] - myList[0])
    return myList
print(Fibona44i(number))
