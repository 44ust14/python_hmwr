# -*-coding: utf-8 -*-
import math

print('Програма знаходить корені рівняння такого типу : ax^2 + bx + c = 0, a ≠ 0')
a = int(input('Введіть змінну a:'))
b = int(input('Введіть змінну b:'))
c = int(input('Введіть змінну c:'))

D = b**2 - 4*a*c

if D < 0:
    print("Дійсних коренів не існує. Існують два комплексних кореня але їх вам знати не потрібно))")
elif D == 0:
    x = (-1 * b)/2 * a
    print('x1 = x2 =', x)
else:
    x1 = (-1 * b + math.sqrt(D))/2 * a
    x2 = (-1 * b - math.sqrt(D))/2 * a
    print('x1=', x1, 'x2=', x2)
