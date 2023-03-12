# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном списке содержащим количество ягод на кустах.
#
#
# Input: 2 2 1 3 2
# Output: 7

from random import randint

n = int(input("Enter n - number of bushes with berries: "))

sequence = [randint(0, 9) for i in range(n)]
print(sequence)

number_of_berries = 0

if n >= 3:
    for i in range(1, n - 1):
        if number_of_berries < (sequence[i - 1] + sequence[i] + sequence[i + 1]): # можно обращаться к отрицательным значениям индекса
            number_of_berries = sequence[i - 1] + sequence[i] + sequence[i + 1]
#       if number_of_berries < (sequence[n - 2] + sequence[n - 1] + sequence[0]):
#           number_of_berries = sequence[n - 2] + sequence[n - 1] + sequence[0]
#       if number_of_berries < (sequence[n - 1] + sequence[0] + sequence[1]):
#           number_of_berries = sequence[n - 1] + sequence[0] + sequence[1]
if n < 3:
    number_of_berries = sum(sequence)

print(number_of_berries)


