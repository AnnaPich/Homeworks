# Задача 18:
# Требуется найти в массиве из случайных чисел(от 1 до n)
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# Последняя строка содержит число X
#
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint

n = int(input("Enter n - number of elements in the array: "))

array = [randint(0, 9) for i in range(n)]
print(array)

x = int(input("Enter number X: "))
flag = True
count = 1
while flag:
    for i in range(n):
        if array[i] == x + count or array[i] == x - count:
            print(f"-> {array[i]}")
            flag = False
    count += 1
