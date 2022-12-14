import openpyxl as opx

def populate(shelf_instance):
    import Task_1
    file = opx.load_workbook('books.xlsx')
    sheet = file['Sheet1']

    for row in sheet.values:
        if row[0] == 'NAME' and row[1] == 'AUTHOR' and row[2] == 'ISBN':
            continue

        else:
            shelf_instance.shelf_arr.append(Task_1.Book(row[0], row[2], row[1]))
