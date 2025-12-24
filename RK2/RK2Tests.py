from unittest import result

from RK2 import *
import pytest

columns = [
    Column(1, "Андреев", 50000, 1),
    Column(2, "Волосатов", 60000, 2),
    Column(3, "Носков", 59452, 3),
    Column(4, "Астроградский", 130000, 3)
]

tables = [
    Table(1, "первый отдел"),
    Table(2, "второй отдел"),
    Table(3, "третий отдел")
]

rows = [
    Row(1, 1,1),
    Row(2, 2,2),
    Row(3, 3,3),
    Row(4, 4,3),
    Row(5, 3,2),
]

def test_Result1():
    result = query_1(columns, tables)

    expected = [{'ColumnSurname': "Андреев", 'TableName': "первый отдел", 'ColumnID': 1, 'TableID': 1},
                {'ColumnSurname': "Астроградский", 'TableName': "третий отдел", 'ColumnID': 4, 'TableID': 3}]

    assert result == expected, (f"Ожидали {expected},получили {result}")

def test_Result2():
    result = query_2(columns, tables)
    expected = [
        ("первый отдел", 50000),
        ("третий отдел", 59452),
        ("второй отдел", 60000)
    ]

    assert result == expected, f"Ожидали {expected}, получили {result}"

def test_Result3():
    result = query_3(columns, tables, rows)

    expected = [
        {'ColumnID': 1, 'ColumnName': 'Андреев',       'TableName': 'первый отдел',       'TableID': 1},
        {'ColumnID': 2, 'ColumnName': 'Волосатов',     'TableName': 'второй отдел', 'TableID': 2},
        {'ColumnID': 3, 'ColumnName': 'Носков',        'TableName': 'третий отдел','TableID': 3},
        {'ColumnID': 4, 'ColumnName': 'Астроградский', 'TableName': 'третий отдел','TableID': 3},
    ]
    assert result == expected, f"Ожидали {expected}, получили {result}"