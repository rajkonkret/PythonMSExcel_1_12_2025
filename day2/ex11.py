import openpyxl

from openpyxl.styles import Font, colors, PatternFill, Border, Side
from openpyxl.formatting.rule import CellIsRule

# wb = openpyxl.load_workbook('video2.xlsx')
# ws = wb.active
#
# print(ws.title)

# zmiana nazwy arkusza
# ws.title = "Video Games Sales Data"
# wb.save('video3.xlsx')
# wb.close()

wb = openpyxl.load_workbook('video3.xlsx')
ws = wb.active
#
# sheet_names = wb.sheetnames
# print(sheet_names)
# # ['Video Games Sales Data', 'Total Sales by Genre', 'Breakdown of Sales by Genre', 'Breakdown of Sales by Year']
#
# # ustawienie aktywnego arkusza po indeksie
# sheet = wb[sheet_names[1]]
# wb.active = wb.index(sheet)

# ws = wb.active
# print(ws.title)  # Total Sales by Genre

ws = wb['Video Games Sales Data']
ws['A1'].font = Font(bold=True, size=12)

wb.save('video3.xlsx')
wb.close()


