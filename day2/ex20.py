import pandas as pd

df = pd.read_excel("excel_from_csv.xlsx")
print(df)
# 3        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167
# pola.rs - przy duzych plikach csv

# filtrowanie danych
print(df[df['Height'] > 175])
#      Name  Height
# 0  Aditya     179
# 1  Sameer     181

suma = df['Height'].sum(skipna=False)  # skipna - omin brakujące, NaN
print(suma)  # 697
