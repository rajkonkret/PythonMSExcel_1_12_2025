import openpyxl

filename = 'video2.xlsx'

wb = openpyxl.load_workbook(filename)
ws = wb['vgsales']

# ws['P1'] = 'Average Sales'
# ws['P2'] = '=AVERAGE(K2:K16328)'
#

# ws['Q1'] = "Number of populated cells"
# ws['Q2'] = "=COUNTA(E2:E16328)"

wb.save(filename)
wb.close()
