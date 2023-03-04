# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# если получается некорректное разделение - напечатать "Неверное S"

number_of_cranes = int(input("Enter number S: "))

if number_of_cranes % 6 == 0:
    number_cranes_Kate = int(number_of_cranes / 3 * 2)
    number_cranes_boys = int((number_of_cranes - number_cranes_Kate) / 2)
    print(f"{number_of_cranes} -> {number_cranes_boys} {number_cranes_Kate} {number_cranes_boys}")
else:
    print("Error! Invalid S!")
