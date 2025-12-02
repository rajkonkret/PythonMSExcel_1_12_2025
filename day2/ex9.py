from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Dane"

headers = ['Miesiąc', "Sprzedaż", "Koszty"]
rows = [
    ["Styczeń", 1200, 800],
    ["Luty", 1200, 800],
    ["Marzec", 1200, 800],
    ["Kwiecień", 1200, 800],
    ["Maj", 1200, 800],
    ["CZerwiec", 1200, 800],
]

ws.append(headers)
for row in rows:
    ws.append(row)

wb.save("wykres.xlsx")
wb.close()
