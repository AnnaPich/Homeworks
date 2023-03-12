# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 списка. 1 строка - первый список через пробел. 2 строка - второй список через пробел.

list_1 = input("Enter a first list of integers separated by a space: ")
list_2 = input("Enter a second list of integers separated by a space: ")

#альтернатива:
# list_1 = set(map(int? input().split())) - сразу преобразуеn в множество, удаляет дубли и сортирует (если данные одного типа)

set_1 = set(list_1.split())
set_2 = set(list_2.split())

set_3 = set_1.union(set_2)
print(set_3)
list_4 = list(set_3)
print(len(list_4))

for i in range(len(list_4)):
    for k in range(len(list_4)):
        if list_4[k] > list_4[i]:
            temp = list_4[k]
            list_4[k] = list_4[i]
            list_4[i] = temp

print(list_4)
