# Задача 12:
# Петя и Катя – брат и сестра.
# Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
#
# Ввод:
# 7
# 12
# Вывод
# 3 4 или 4 3

sum = int(input("Enter sum two numbers: "))
mult = int(input("Enter multiplication two numbers: "))

discr = sum ** 2 - 4 * mult  # discriminant

if discr > 0:
    x = (sum + discr ** (1 / 2)) / 2
    y = (sum - discr ** (1 / 2)) / 2
    print(f"first number: {x}, second number: {y}")
elif discr == 0:
    x = sum / (2 * mult)
    print(f"number: {x}")
else:
    print(f"there are no solutions.")