# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек
# отломить k долек, если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no

size_n = int(input("Enter the length of the chocolate bar: "))
size_m = int(input("Enter the width of the chocolate bar: "))
k = int(input("Enter the required number of pieces of chocolate: "))

if k % size_n == 0 or k % size_m == 0 and (n*m >= k):
    print(f"{size_n} {size_m} {k} -> yes")
else:
    print(f"{size_n} {size_m} {k} -> no")