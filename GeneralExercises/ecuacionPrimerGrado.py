'''
Crear un Algoritmo que permita hallar la solución a una ecuación de primer grado, de la forma: ax + b = 0
'''
import math

print(f'Ecuacion de primer grado: ax + b = 0')
a = int(input('Ingrese el valor de a (con a diferente de 0): '))
b = int(input('Ingrese el valor de b: '))

print(f'La ecuacion de primer grado es: ({a})x + ({b}) = 0')

if a == 0:
    raise ValueError('El valor de a no debe ser 0')
x = 0
if b < 0:
    x = math.fabs(b) / a
else:
    x = (-1 * b) / a

print(f'El valor de x es: {x}')