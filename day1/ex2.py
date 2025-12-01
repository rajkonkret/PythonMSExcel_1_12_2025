# wczytanie pliku excel
from openpyxl import Workbook, load_workbook

workbook = load_workbook('sample.xlsx')
sheet = workbook.active
print(sheet) # <Worksheet "Sheet">