
class Column:
    def __init__(self, ID, Surname, Salary, table_ID):
        self.ID = ID
        self.Surname = Surname
        self.Salary = Salary
        self.table_ID = table_ID
    def __repr__(self):
        return f"Column(ID={self.ID}, Surname={self.Surname}, Salary={self.Salary}, table_ID={self.table_ID})"

class Table:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
    def __repr__(self):
        return f"Table(ID={self.ID}, name={self.name})"

class Row:
    def __init__(self, id_row, column_id, table_id):
        self.ID = id_row
        self.column_ID = column_id
        self.table_ID = table_id
    def __repr__(self):
        return f"Row(id_row={self.ID}, column_id={self.column_ID}, table_ID={self.table_ID})"

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
    Row(1, 1,1),
    Row(2, 2,2),
    Row(3, 3,3),
    Row(4, 4,3),
    Row(5, 3,2),
]

def query_1(columns, tables):
    ColumnA = [i for i in columns if i.Surname.startswith("А")]

    result = list(map(lambda i: {
        "ColumnSurname": i.Surname,
        "TableName": next((T.name for T in tables if T.ID == i.table_ID), None),
        "ColumnID": i.ID,
        "TableID": i.table_ID
    }, ColumnA))

    return result

def query_2(columns, tables):

    MinCharsPerTable = {
        TableObj.name: min(S.Salary for S in columns if S.ID == TableObj.ID)
        for TableObj in tables
        if any(S.ID == TableObj.ID for S in columns)
    }
    SortedResult = sorted(MinCharsPerTable.items(), key=lambda X: X[1])
    return SortedResult

def query_3(columns, tables, rows):
    result = [
        {
            'ColumnID': Column.ID,
            'ColumnName' : Column.Surname,
            'TableName': TableObj.name,
            'TableID': TableObj.ID
        }
        for i in rows
        for Column in columns if Column.ID == i.ID
        for TableObj in tables if TableObj.ID == i.table_ID
    ]
    SortResult = sorted(result, key=lambda X: X['ColumnID'])
    return SortResult

def main():
        print("Запрос 1 (фамилии на 'А' и их таблицы): ")
        result1 = query_1(columns, tables)
        for i in result1:
            print(f"Столбец: {i['ColumnSurname']}, Таблица: {i['TableName']}")

        print("\nЗапрос 2 (минимальные зарплаты по отделам):")
        result2 = query_2(columns, tables)
        for TableName, MinCost in result2:
            print(f"Таблица: {TableName}, зарплата: {MinCost}")

        print("\nЗапрос 3 (все строки и их таблицы):")
        result3 = query_3(columns, tables, rows)
        for i in result3:
            print(f"ID столбца: {i['ColumnID']}, Столбец: {i['ColumnName']}, Таблица: {i['TableName']}")
main()