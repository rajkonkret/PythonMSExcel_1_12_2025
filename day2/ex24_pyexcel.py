import pyexcel

#  pip install pyexcel pyexcel-xlsx

data = [
    ["Imię", "Wiek"],
    ["Tomek", 38],
    ['Kasia', 37],
]

sheet = pyexcel.Sheet(data)
sheet.save_as('wyniki.xlsx')
