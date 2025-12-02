import openpyxl
from openpyxl.chart import Reference, BarChart
from openpyxl.chart.axis import ChartLines

wb = openpyxl.load_workbook('wykres.xlsx')
ws = wb['Dane']

data = Reference(ws,
                 min_col=2,
                 max_col=3,
                 min_row=1,
                 max_row=7)

cats = Reference(ws,
                 min_col=1,
                 max_col=1,
                 min_row=2,
                 max_row=7)

chart = BarChart()
chart.add_data(data, titles_from_data=True)
chart.set_categories(cats)  # wypełnienie legendy

chart.title = "Sprzedaż"
chart.x_axis.title = "Sprzedaż"
chart.y_axis.title = "Miesiąc"

chart.legend.position = "r"  # prawa strona
# chart.legend.position = "t" # top
# chart.legend.position = "tr" # top-right
# chart.legend.position = "b" # bottom

chart.legend.overlay = False  # dodakowa przestrzeń ma legende
chart.width = 20  # wielkośc wykresu
chart.height = 10

ws.add_chart(chart, "E2")

wb.save("wykres2.xlsx")
wb.close()
