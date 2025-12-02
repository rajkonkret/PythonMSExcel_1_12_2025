# wczytac plik
# wybrac dowolny arkusz
from openpyxl import load_workbook
import pandas as pd

# wb = load_workbook('excel_with_multiple_sheets.xlsx')
# ws = wb.active
# ws = wb['marks']
#
# print(ws) # <Worksheet "marks">

df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name=2)  # indeksy
print("The dataframe is:")
print(df)
# The dataframe is:
#     Name  Marks
# 0  Adiya    179
# 1  Samen    181
# 2  Darek    170
# 3   Jhon    167

df = pd.read_excel("excel_with_multiple_sheets.xlsx", sheet_name="marks")
print("The dataframe is:")
print(df)
# The dataframe is:
#     Name  Marks
# 0  Adiya    179
# 1  Samen    181
# 2  Darek    170
# 3   Jhon    167