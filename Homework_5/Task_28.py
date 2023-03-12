# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4


def sum_a_b(a, b):
    if b == 0:
        return a
    return (sum_a_b(a + 1, b - 1))


numb_a = int(input("Enter number A: "))
numb_b = int(input("Enter number B: "))

print(f'a = {numb_a}, b = {numb_b} -> {sum_a_b(numb_a, numb_b)}')