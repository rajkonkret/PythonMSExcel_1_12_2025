# xlwings
# wymaga excela

import xlwings as xw
import pandas as pd
import numpy as np

df = pd.DataFrame(data=np.random.rand(100, 5),
                  columns=[f"Próba {i}" for i in range(1, 6)])

print(df)
print(df.head())  # pięć pierwszych
print(df.tail())

# xw.view(df)

book = xw.Book()
print(book.name)  # Zeszyt1
print(book.sheets)  # Sheets([<Sheet [Zeszyt1]Arkusz1>])

sheet1 = book.sheets[0]
print(sheet1.range('A1'))
# <Range [Zeszyt1]Arkusz1!$A$1>

sheet1.range('A1').value = [[1, 2],
                            [3, 4]]
sheet1.range('A4').value = "Witaj!"

print(sheet1["A1:B2"].value)
# [[1.0, 2.0], [3.0, 4.0]]
