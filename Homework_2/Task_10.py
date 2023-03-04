# Задача 10:
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
#
# 1 - герб, 0 - решка
# Ввод:
# 4 - число монет
# 0
# 1
# 1
# 1
# Вывод: 1

number_coins = int(input("Enter number of coins: "))
count = 0
from random import randint
for i in range(number_coins):
    coin_side = randint(0, 1)
    print(f"side of coin: {coin_side}")
    if coin_side == 0:
        count += 1
if count <= number_coins/2:
    print(f"it is necessary to flip {count} coins")
else:
    print(f"it is necessary to flip {n-count} coins")