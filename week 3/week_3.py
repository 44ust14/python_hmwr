# -*- coding:utf-8 -*-

polindrom = input('Input word:')
reverse_polindrom = polindrom[::-1]
def is_polindrom():
    if len(polindrom) == 0:
        print("Error. String is empty.")
    elif len(polindrom) > 100:
        print("Error. String is longer than 100 symbols.")
    elif polindrom == reverse_polindrom:
        print("True")
    else:
        print("False")

is_polindrom()
