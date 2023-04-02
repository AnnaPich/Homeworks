def input_data(FILENAME):  # функция ввода данных
    with open(FILENAME, 'a', encoding='utf-8') as file:
        file.write(input("Введите данные: " + "\n"))
        ##file.write(f'\n{info}')
        print("Данные добавлены")


def show_data(FILENAME) -> str:  # функция показа справочника
    with open(FILENAME, 'r', encoding='utf-8') as data:
        book = data.read().split('\n')
    return book


# print(book.split('\n'))

def find_data(FILENAME):
    with open(FILENAME, 'r', encoding='utf-8') as data:
        text = data.read().split('\n')
        request = input("Введите запрос для поиска: ")
        result = [(text.index(book), book)
                  for book in text if request.lower() in book.lower()]
        if len(result) >= 1:
            print("Найдены следующие данные: ")
            [print(f'{result.index(book) + 1} {str(book[1])}')
             for book in result]
            return ([line[0] for line in result], text)
        else:
            print("Значение ненайдено")
            return ([], text)

        # for i in text:
        #     if i == request:
        #         count += 1
        #         print(f'\n{i}')
        # if count == 0:
        #     print("Введенные данные не найдены, повторите запрос.")
        # pass


def replacement_data(FILENAME):
    data = find_data(FILENAME)
    if len(data[0]) == 1:
        rewrite(data[0][0], data[1], FILENAME)
    elif len(data[0]) > 1:
        change = int(
            input("Введите порядковый номер изменяемой записи: "))
        while change not in [i for i in range(i, len(data[0] + 1))]:
            print("Данные не найдены")
            change = int(
                input("Введите порядковый номер изменяемой записи: "))
        rewrite(int(data[0][change - 1]), data[1], FILENAME)


def delete_data(FILENAME):
    data = find_data(FILENAME)
    if len(data[0]) == 1:
        delete(data[0][0], data[1], FILENAME)
    elif len(data[0]) > 1:
        change = int(
            input("Введите порядковый номер удаляемой записи: "))
        while change not in [i for i in range(i, len(data[0] + 1))]:
            print("Данные не найдены")
            change = int(
                input("Введите порядковый номер удаляемой записи: "))
        delete(int(data[0][change - 1]), data[1], FILENAME)


def rewrite(strings, data, FILENAME):
    fio = input("Введите откорректированные ФИО: ")
    n_phone = input("Введите откорректированный номер: ")
    with open(FILENAME, 'w', encoding='utf-8') as file:
        [file.write(f'{fio} | {n_phone}\n') if line == strings else file.write(
            f'{data[line]}\n') for line in range(len(data) - 1)]
    print("Данные успешно изменены")


def delete(strings, data, FILENAME):
    with open(FILENAME, 'w', encoding='utf-8') as file:
        [file.write(f'{data[line]}\n') if line !=
         strings else '' for line in range(len(data) - 1)]
        print("Данные успешно удалены")