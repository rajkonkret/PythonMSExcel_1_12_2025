import pandas as pd

df = pd.DataFrame({
    "Imie": ['Jan', "Anna", "Tomek"],
    "Wiek": [29, 24, 35],
    "Miasto": ['Warszawa', "Wrocław", "Legnica"]
})

# kontekst menadzer - bezpieczniejsza praca z plikiem
with pd.ExcelWriter("Tabela.xlsx", engine='xlsxwriter') as writer:
    df.to_excel(writer, sheet_name="Osoby", startrow=1, header=False, index=False)

    workbook = writer.book
    worksheet = writer.sheets['Osoby']

    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'vcenter',
        'bg_color': '#D7E4BC'
    })

    # enumerate() - numeruje kolekcje
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)

    (max_row, max_col) = df.shape  # odczytujemy kształt tablicy

    # chr() - znak o wskazanym kodzie chr(65) -> A
    cell_range = f'A1:{chr(65 + max_col - 1)}{max_row + 1}'  # "A1:A1"

    worksheet.add_table(cell_range, {
        'name': "TabelaOsoby",
        "columns": [{"header": col} for col in df.columns]
    })
# nie muszę robic wb.close() bo używam kontekst menadżera
