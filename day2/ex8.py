import openpyxl
from openpyxl.chart import Reference, BarChart
from openpyxl.chart.axis import ChartLines

wb = openpyxl.load_workbook('video2.xlsx')
ws = wb['Total Sales by Genre']

# wycinamy dane potrzebne z excela do zrobienia wykresu
values = Reference(ws,
                   min_col=2,
                   max_col=2,
                   min_row=1,
                   max_row=13)

cats = Reference(ws,
                 min_col=1,
                 max_col=1,
                 min_row=2,
                 max_row=13)
