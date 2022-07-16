'''
Задача 1
Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
'''
list_number = [1,43,6,43,346,6,464,64,423,7,568,]
new_list = []
count = 0
for i in list_number:
    if count % 2 == 1:
        new_list.append(i)
    count+=1
print(f'На нечётных позициях стоят числа {new_list}')
print(f'Сумма = {sum(new_list)}')
'''
Задача 2
Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
'''
list_number2 = [2, 3, 4, 5, 6]
count = 0
new_list = []
for i in list_number2:
    if count < len(list_number2)/2:
        count += 1
        new_list.append(list_number2[-count] * i)
    else:
        break
print(new_list)
'''
Задача 3
Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
между максимальным и минимальным значением дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
'''
list_number3 = [1.1, 1.2, 3.1, 5, 10.01]
new_numbers = []
number = 0
for i in list_number3:
    new_numbers.append(i - int(i))
number = max(new_numbers)-min(new_numbers)
print(number)
'''
Задача 4
Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10
'''
number = int(input())
bin(number)
print(format(number, 'b'))
# Либо
st = ''
while number > 0:
    st = str(number % 2) + st
    number = number//2
print(st)
'''
Задача 5
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
*Пример:*
- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
'''
fibonachi = int(input())
list_fib = [0,1]
fib1 = 0
fib2 = 1
fibsum = 0
list_negative = [1]
cw = []
if fibonachi > 2:
    for i in range(0,fibonachi-1):
        fibsum = fib1 + fib2
        list_fib.append(fibsum)
        list_negative.append(fibsum * -1)
        fib1 = fib2
        fib2 = fibsum
    sorted(list_negative)
    list_negative.reverse()
    cw = list_negative + list_fib
elif fibonachi == 1:
    cw = [-1,0,1]
else:
    cw = 0
print(cw)