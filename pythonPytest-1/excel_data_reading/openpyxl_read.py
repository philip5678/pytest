import openpyxl

book = openpyxl.load_workbook('./test_data.xlsx')

sheet = book.active

a1 = sheet['add_test']
a2 = sheet['add_test-1']
a3 = sheet.cell(row=3, column=1)

print(a1.value)
print(a2.value)
print(a3.value)