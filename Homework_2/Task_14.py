# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
#
# Ввод:
# 6
# Вывод
# 1 2 4
# Ввод
# 24
# Вывод
# 1 2 4 8 16

number = int(input("Enter number N: "))
i = 0
if number >= 2:
    for i in range(number):    # or another solution: while 2 ** i <= n:
        two_exp = 2 ** i
        if two_exp < number:
            print(two_exp)
else:
    print("incorrect input")


