import openpyxl

from openpyxl.styles import Font, colors, PatternFill, Border, Side
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles.fills import FILL_PATTERN_DARKUP

wb = openpyxl.load_workbook('video3.xlsx')
ws = wb.active

print(ws.title)
