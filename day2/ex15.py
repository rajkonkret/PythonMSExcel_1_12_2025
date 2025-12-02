import pandas as pd

#  pip install xlsxwriter
data = [
    ["Adiya", 179],
    ["Samen", 181],
    ["Darek", 170],
    ["Jan", 167],
]

column_names = ['Name', "Height"]

df = pd.DataFrame(data, columns=column_names)


writer = pd.ExcelWriter("excel_with_list.xlsx", engine="xlsxwriter")
# sprawdzenie wyłaczenia pogrubienia kolumn

# df.to_excel(writer)
# df.to_excel(writer, index=False)  # bez kolumny index
df.to_excel(writer, index=False, sheet_name='first_sheet')  # nazwa arkusza
writer.close()
