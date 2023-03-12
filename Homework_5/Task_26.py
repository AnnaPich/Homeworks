# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую неотрицательную степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

def degree_A(a, b, c):
    if b == 0:
        return c
    return (degree_A(a, (b - 1), (a * c)))


numb_a = int(input("Enter number A: "))
numb_b = int(input("Enter number B: "))
extent = 1

print(f'A = {numb_a}, B = {numb_b} -> {degree_A(numb_a, numb_b, extent)}')

