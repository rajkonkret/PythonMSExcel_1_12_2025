import openpyxl

wb = openpyxl.load_workbook(r"video2.xlsx")
ws = wb.active

ws = wb['vgsales']

wb.save("video2.xlsx")
wb.close()