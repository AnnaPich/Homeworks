# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве из случайных чисел.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint

n = int(input("Enter N - number of elements in the array: "))

array = [randint(0, 9) for i in range(n)]
print(array)

x = int(input("Enter number X: "))

count = 0
for i in range(n):
    if array[i] == x:
        count += 1
print(f"-> {count}")
