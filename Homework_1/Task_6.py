# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# *Пример:*
#
# 385916 -> yes
# 123456 -> no

number_ticket = input("enter a six-digit number: ")

summ_one_half_ticket = int(number_ticket[0]) + int(number_ticket[1]) + int(number_ticket[2])
summ_two_half_ticket = int(number_ticket[3]) + int(number_ticket[4]) + int(number_ticket[5])

if summ_one_half_ticket == summ_two_half_ticket:
    print(f"{number_ticket} -> yes")
else:
    print(f"{number_ticket} -> no")