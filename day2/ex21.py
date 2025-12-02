# stworzyc plik z danymi: sprzedaz_dane.xlsx
# wczytac ten plik
# przetworzyc te dane: ilosc * cena
# dodc kolumne
# dopisac te wyniki

# dane
import pandas as pd

data = {
    "Produkt": ["Laptop", "Myszka", "Laptop", "Monitor", "Myszka", "Klawiatura"],
    "Ilość": [2, 5, 1, 1, 3, 2],
    "Cena_jedn": [3500, 80, 3600, 900, 75, 120],
}

df = pd.DataFrame(data)
wejscie = "sprzedaz_dane.xlsx"
df.to_excel(wejscie, index=False)

df = pd.read_excel(wejscie)

df['Wartość'] = df['Ilość'] * df['Cena_jedn']

# zwróci dataframe
podsumowanie = (
    df.groupby("Produkt")[["Ilość", "Wartość"]]
    .sum()
    .reset_index()
    .sort_values(by="Wartość", ascending=False)
)

wyjscie = "raport_sprzedaz.xlsx"
with pd.ExcelWriter(wyjscie, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Dane", index=False)
    podsumowanie.to_excel(writer, sheet_name="Podsumowanie", index=False)

print('plik został zapiany:', wyjscie)
