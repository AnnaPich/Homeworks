# Задача 32:
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def new_array (array, number_min, number_max):
    new_ar = list()
    for i in range(len(array)):
        if number_max >= array[i] >= number_min:
            new_ar.append(array[i])
    return (new_ar)


from random import randint

array = [randint(0, 9) for i in range(10)]
print(array)

number_min = int(input("Enter minimum number: "))
number_max = int(input("Enter maximum number: "))

print(new_array (array, number_min, number_max))
