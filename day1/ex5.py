import openpyxl

filename = "video2.xlsx"

wb = openpyxl.load_workbook(filename)
ws = wb.active

ws = wb['vgsales']

wb.save(filename)
wb.close()
