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
