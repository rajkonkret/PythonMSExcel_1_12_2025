import openpyxl

from openpyxl.styles import Font, colors, PatternFill, Border, Side
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles.fills import FILL_PATTERN_DARKUP

wb = openpyxl.load_workbook('video3.xlsx')
ws = wb.active

print(ws.title)

# rgb -> FF0000 -> red
ws['A1'].font = Font(color="FF0000", bold=True, size=12)
ws['A2'].font = Font(color="0000FF")

wb.save('video3.xlsx')
wb.close()