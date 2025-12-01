# https://peps.python.org/pep-0008/
# snake_case
import sys

# ctrl alt l - formatowanie
print("Radek")  # wydrukuj/wypisz, Radek
print("")
print("")
print('Radek')  # Radek

# ctrl / - komentarz
# print("Radek')
#   File "C:\Users\CSComarch\PycharmProjects\PythonMSExcel_1_12_2025\pierwszy.py", line 10
#     print("Radek')
#           ^
# SyntaxError: unterminated string literal (detected at line 10)
#
# Process finished with exit code 1

# type()
# typowanie dynamiczne
print(type("Radek"))  # <class 'str'>, tekst

print(45)
print(type(45))  # <class 'int'>, liczby całkowite

print(sys.int_info)
# sys.int_info(bits_per_digit=30, sizeof_digit=4, default_max_str_digits=4300,
# str_digits_check_threshold=640)

print("34" + "19")  # 3419, konkatenacja, łączenie stringów

print(34 + 19)  # 53

# print("35" + 29)  # TypeError: can only concatenate str (not "int") to str

print(34 * "168")
print(34 * 168)

print(10 * "-")  # ----------

print(4.56)  # liczby zmiennoprzecinkowe
print(type(4.56))  # <class 'float'>
print(sys.float_info)
# sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308,
# min=2.2250738585072014e-308, min_exp=-1021
# , min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

# błąd zaokrąglenia
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.9)  # 1.0
# decimal - pozwala ominąc problem zokrąglenia

# zmienna - pudełko dane
# typowanie dynamiczne
name = "Radek"
print(name)  # Radek
name = 90
print(name)  # 90
# print(name + "Kowalski")

a = "1"
b = 0
# print(a + b)  # TypeError: can only concatenate str (not "int") to str

# rzutownie - int() - zamiana na całkowite
print(int(a) + int(b))  # 1

# teksty są niemutowalne
tekst = "Witaj Świecie"

# """ Return a copy of the string converted to uppercase. """
tekst.upper()  # nie zmienia oryginału
print(tekst)  # Witaj Świecie
print(tekst.upper())  # WITAJ ŚWIECIE
nowy_tekst = tekst.upper()
print(nowy_tekst)  # WITAJ ŚWIECIE

zmienna1 = "GROSS"  # gross
zmienna2 = "groẞ"

print(zmienna1.lower() == zmienna2.lower())  # == porównanie, False
print(zmienna1.casefold() == zmienna2.casefold())  # True

# typ logiczny, True, False
print(1 != 0)  # != - różne

name = "Radek"
# f - f string, string sformatowany
print(f"Nazywam się: {name} ")  # Nazywam się: {name}  -> Nazywam się: Radek

a = 4.567
print(f"Liczba: {a}")  # Liczba: 4.567
# ctrl d - powielanie linii
print(f"Liczba: {a:.2f}")  # Liczba: 4.57 - zaokrąglił wypisywania

# - float
# %f - float
print("Liczba: %f" % a)  # Liczba: 4.567000
print("Liczba: %.2f" % a)  # Liczba: 4.57
print("Liczba: %.1f" % a)  # Liczba: 4.6
print("Liczba: %.0f" % a)  # Liczba: 5
print("Liczba: %.f" % a)  # Liczba: 5
# print("Liczba: %.f" % "Radek")  # TypeError: must be real number, not str, sprawdza typy

print("""
Tekst
    wielolinijkowy""")
# Tekst
#     wielolinijkowy
print("""
    
        
        
        """)

#
"""Komentarz
    wielolinijkowe - dokumentacja"""

print(100 / 3)  # 33.333333333333336
print(100 // 3)  # 33 - częśc cąlkowita z dzielenia
print(100 % 3)  # modulo, reszta z dzielenia 33 * 3 = 99, 100 - 99 = 1 reszta = 1
print(10 % 2)  # parzysta, reszta z dzielenia przez 2 jest 0

zysk = 890123456765123
print(f"Nasza duża liczba: {zysk:,} ")  # Nasza duża liczba: 890,123,456,765,123
print(f"Nasza duża liczba: {zysk:_} ")  # Nasza duża liczba: 890_123_456_765_123
print(f"Nasza duża liczba: {zysk:_} ".replace("_", " "))  # Nasza duża liczba: 890 123 456 765 123
print(f"Nasza duża liczba: {zysk:_} ".replace("_", "."))  # Nasza duża liczba: 890.123.456.765.123

liczba = 15_000_000_000_000
print(liczba)  # 15000000000000
print(type(liczba))  # <class 'int'>
# https://naukapythona.com.pl/

# kolekcje - przechowuje wiele danych

# lista - dowolne typy na raz, zachowuje kolejność
lista = [1, 2, 3, 4, 5, 6, "Radek"]
print(type(lista))  # <class 'list'>
print(lista)  # [1, 2, 3, 4, 5, 6, 'Radek']

lista = []  # pusta lista

lista.append("Radek")
lista.append("Tomek")
lista.append("Miłka")
lista.append("Kaludia")
lista.append("Zenek")
print(lista)  # ['Radek', 'Tomek', 'Miłka', 'Kaludia', 'Zenek']

# usuniecie
lista.remove("Radek")
print(lista)  # ['Tomek', 'Miłka', 'Kaludia', 'Zenek']

lista_copy = lista.copy()
lista_k = lista  # kopia referencji, kopia adresu listy
print(lista_k)  # ['Tomek', 'Miłka', 'Kaludia', 'Zenek']
print(lista)  # ['Tomek', 'Miłka', 'Kaludia', 'Zenek']

lista.clear()  # usunięcie eleemntów z listy o nazwie: lista
print(lista)  # []
print(lista_k)  # []
print(lista_copy)  # ['Tomek', 'Miłka', 'Kaludia', 'Zenek']

# krotka (tupla) - niemutowalna lista, do odczytu
# pozwala lepiej zarzadzac pamięcią
krotka = tuple(lista_copy)
print(krotka)  # ('Tomek', 'Miłka', 'Kaludia', 'Zenek')
tupla1 = "Radek", "Tomek"
print(type(tupla1))  # <class 'tuple'>
tupla_jeden = "Radek",
print(type(tupla_jeden))  # <class 'tuple'>

# zbiór - set()
# przechowuje unikalne wartości
# brak duplikatów
# nie zachowuje kolejnosci
lista = [2, 5, 6, 8, 6, 7, 8, 5, 9]
zbior = set(lista)
print(zbior)  # {2, 5, 6, 7, 8, 9}
print(type(zbior))  # <class 'set'>
pusty_zbior = set()
print(pusty_zbior)  # set()
pusty_zbior.add(15)
print(pusty_zbior)  # {15}

zbior1 = {5, 6, 8}
print(zbior.intersection(zbior1))  # {8, 5, 6}, część wspólna zbiorów
print(zbior & zbior1)  # {8, 5, 6}, część wspólna zbiorów

# słownik - klucz - wartossc
slownik = {'name': "Radek", "age": 56}
print(slownik)  # {'name': 'Radek', 'age': 56}
print(type(slownik))  # <class 'dict'>

pusty_slownik = {}
print(type(pusty_slownik))  # <class 'dict'>
print(pusty_slownik)  # {}

# wypisanie danych po indeksie
# od 0
lista = [1, 2, 3, 4, 5, 6, "Radek"]
print(lista[0])
print(lista[2])
print(lista[6])  # Radek
print(lista[-1])  # ostatni element

tupla1 = "Radek", "Tomek", "Zenek"
print(tupla1[1])  # Tomek

slownik = {'name': "Radek", "age": 56}
print(slownik['name'])  # Radek

print(slownik.keys())
print(slownik.values())
print(slownik.items())
# dict_keys(['name', 'age'])
# dict_values(['Radek', 56])
# dict_items([('name', 'Radek'), ('age', 56)])
slownik = {1: "Radek", "age": 56}
print(slownik[1])  # Radek

# warunek
odp = "Radek"
if odp == "Radek":
    print("Ok")  # 4 space
elif odp == "Tomek":
    print("Tomek")
else:
    print("inny")

# # od python 3.10
# odp = input("Podja znany Ci język programowania")
#
# # strip() - usunięcie białych znaków
# match odp.casefold().strip():
#     case "python":
#         print("Lubię pythona")
#     case "java":
#         print("Lubię jave")
#     case _:  # zastępuje elsee
#         print("Inny")

# pętle
for i in range(5):  # od 0 do 4
    print(i)
# 0
# 1
# 2
# 3
# 4

for i in lista:
    print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# Radek

for i in range(5):
    print('Radek')
    print(i)
    print("Wykonane w pętli")
print("Poza pętlą")
# 3
# Wykonane w pętli
# Radek
# 4
# Wykonane w pętli
# Poza pętlą

# pętla sterowana warunkiem - while
licznik = 0
while licznik < 10:
    print("Komunikat")
    licznik += 1  # licznik = licznik + 1

# list comprehensions
print([x * 2 for x in {1, 2, 3, 4, 5}])
# [2, 4, 6, 8, 10]
l1 = []
for x in {1, 2, 3, 4, 5}:
    l1.append(x * 2)
print(l1)  # [2, 4, 6, 8, 10]
