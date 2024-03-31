import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    Добавление нового пользователя.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    Возвращает все содержимое телефонной книги.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    Поиск записи по критерию data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "По указанному значению совпадений не найдено"
    return "\n".join(result)


def transfer_data(filename: str, new_file: str, num_row: int):
    """
    Функция  для переноса указанной строки из одного файла
    в другой
    source: str - имя исходного файла
    dest: str - имя файла куда переносим
    num_row: int - номер переносимой строки
    """

    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split('\n')

    with open(new_file, "w", encoding="utf-8") as new_file:
        new_file.write(list_1[num_row - 1])

    return 0

def phonebook_show(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split('\n')
        count = 0
        iter = []

    with open(filename, "r", encoding="utf-8") as file:
        for i in file.read().split("\n"):
            count += 1
        for i in range(1, count + 1):
            iter.append(i)

        ph_strochno = {k:v for k, v in zip(iter, list_1)}
        for i in ph_strochno.keys():
            print(f"{i}: {ph_strochno[i]}")


INFO_STRING = """
Выберите режим работы:
1 - вывести все данные
2 - добавление нового пользователя
3 - поиск
4 - перенос записи в другой файл
0 - выход
"""

file = "text.txt"

if file not in os.listdir():
    print("указанное имя файла отсутствует")
    sys.exit()


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
    elif mode == 2:
        name = input("Введите Ваше имя: ")
        phone = input("Введите Ваш телефон: ")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("Введите значение: ")
        print(search_user(file, data))
    elif mode == 4:
        phonebook_show(file)
        new_file = input("Введите имя новой телефонной книги: ")
        num_row = int(input("Введите номер строки, которую хотите скопировать в новую телефонную книгу: "))
        transfer_data(file, new_file, num_row)
        print("Строка скопирована в новую телефонную книгу.")
    elif mode == 0:
        exit()