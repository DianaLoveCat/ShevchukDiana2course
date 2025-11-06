
class Column:
    def __init__(self, ID, Surname, Salary, table_ID):
        self.ID = ID
        self.Surname = Surname
        self.Salary = Salary
        self.table_ID = table_ID

class Table:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

class Row:
    def __init__(self, id_row, column_id):
        self.id_row = id_row
        self.column_id = column_id

# Списки объектов

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
    Row(1, 1),
    Row(2, 2),
    Row(3, 3),
    Row(4, 4),
]

def query_1():
    result = []
    for row in rows:
        col = next((c for c in columns if c.ID == row.column_id), None)
        if col and col.Surname.startswith("А"):
            tbl = next((t for t in tables if t.ID == col.table_ID), None)
            if tbl:
                result.append((row.id_row, col.Surname, tbl.name))
    return result

def query_2():
    MinCharsPerTable = {
        TableObj.name: min(S.Salary for S in columns if S.ID == TableObj.ID)
        for TableObj in tables
        if any(S.ID == TableObj.ID for S in columns)
    }
    SortedResult = sorted(MinCharsPerTable.items(), key=lambda X: X[1])
    return SortedResult

def query_3():
    result = []
    for row in sorted(rows, key=lambda r:  r.id_row):
        col = next(c for c in columns if c.ID == row.column_id)
        tbl = next(t for t in tables if t.ID == col.table_ID)
        result.append((row.id_row, col.Surname, tbl.name))
    return result

print("Запрос 1 (фамилии на 'А' и их таблицы): ")
for id_row, surname, tbl_name in query_1():
    print(f"Фамилия: {surname}, Таблица: {tbl_name}")

print("\nЗапрос 2 (минимальные зарплаты по отделам):")
print(query_2())

print("\nЗапрос 3 (все строки и их таблицы):")
for id_row, surname, tbl_name in query_3():
    print(f"Фамилия: {surname}, Таблица: {tbl_name}")
