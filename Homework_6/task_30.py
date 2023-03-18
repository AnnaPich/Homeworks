# Задача 30:
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def array_arithm_progression(x, y, z):
    array = list()
    array.append(y)
    for i in range(2, x + 1):
        array.append(y + (i - 1) * z)
    return (array)


quantity = int(input("Enter quantity elements: "))
first_element = int(input("Enter a first element: "))
difference = int(input("Enter a difference of arithmetic progression: "))

print(array_arithm_progression(quantity, first_element, difference))
