import os
import sys


def add_new_user(name: str, phone: str, filename: str):
    """
    ���������� ������ ������������.
    """
    new_line = '\n' if read_all(filename) != "" else ''
    with open(filename, "a", encoding="utf-8") as file:
        file.write(f"{new_line}{name} - {phone}")


def read_all(filename: str) -> str:
    """
    ���������� ��� ���������� ���������� �����.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def search_user(filename: str, data: str) -> str:
    """
    ����� ������ �� �������� data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        list_1 = file.read().split("\n")
    result = []
    result = [i for i in list_1 if data in i]
    if not result:
        return "�� ���������� �������� ���������� �� �������"
    return "\n".join(result)


def transfer_data(filename: str, new_file: str, num_row: int):
    """
    �������  ��� �������� ��������� ������ �� ������ �����
    � ������
    source: str - ��� ��������� �����
    dest: str - ��� ����� ���� ���������
    num_row: int - ����� ����������� ������
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
�������� ����� ������:
1 - ������� ��� ������
2 - ���������� ������ ������������
3 - �����
4 - ������� ������ � ������ ����
0 - �����
"""

file = "text.txt"

if file not in os.listdir():
    print("��������� ��� ����� �����������")
    sys.exit()


while True:
    mode = int(input(INFO_STRING))
    if mode == 1:
        print(read_all(file))
    elif mode == 2:
        name = input("������� ���� ���: ")
        phone = input("������� ��� �������: ")
        add_new_user(name, phone, file)
    elif mode == 3:
        data = input("������� ��������: ")
        print(search_user(file, data))
    elif mode == 4:
        phonebook_show(file)
        new_file = input("������� ��� ����� ���������� �����: ")
        num_row = int(input("������� ����� ������, ������� ������ ����������� � ����� ���������� �����: "))
        transfer_data(file, new_file, num_row)
        print("������ ����������� � ����� ���������� �����.")
    elif mode == 0:
        exit()