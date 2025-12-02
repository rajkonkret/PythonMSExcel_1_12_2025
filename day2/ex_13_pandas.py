# pandas - biblioteka do danych tabelarycznych
# DataFrame - odpowiednik tablicy/ macierzy
import pandas as pd

# pip install pandas

writer = pd.ExcelWriter('empty_excel.xlsx')
empty_dataframe = pd.DataFrame()  # tablica/ macierz

empty_dataframe.to_excelwriter(sheet_name='empty')
writer.close()  # przy pracy z writerem musimy używać close()
