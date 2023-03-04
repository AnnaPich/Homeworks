# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

number = input("enter a three-digit number: ")
digit_one = int(number[0])
digit_two = int(number[1])
digit_three = int(number[2])

summ = digit_one + digit_two + digit_three

print(f"{number} -> {summ} ({digit_one} + {digit_two} + {digit_three})")
