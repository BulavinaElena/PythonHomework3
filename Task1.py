#Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#Пример:
#[2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12

result=0
numbers=[1, 5, 8, 15]
for i in range(len(numbers)):
    if i%2==1:
        result+=numbers[i]
print(result)