# pip - manager pakietów pythona
# pip install openpyxl

from openpyxl import Workbook, load_workbook

wb = Workbook()  # szablon pliku excel
ws = wb.active  # ustawia aktywny arkusz

# komórka A1 w arkuszu
ws['A1'] = 42

# zapisanie danych do pliku excel
wb.save("sample.xlsx")
wb.close()
