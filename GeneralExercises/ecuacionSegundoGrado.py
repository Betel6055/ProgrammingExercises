'''
Crear un Algoritmo que permita hallar la solución a una ecuación de segundo grado, de la forma:
ax^2 + bx + c = 0
'''
import math

print('Solucion a la ecuacion de segundo grado del tipo: ax^2 + bx + c = 0\n')

a = int(input('Ingrese el valor de a (con a diferentes de 0): '))
b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c: '))

if (4 * a * c) > math.pow(b, 2):
    print('La reiz se encuentra en el dominio de los imaginarios.')
else:
    x1 = ((-1 * b) + math.sqrt(math.pow(b, 2) - (4 * a * c)))/(2 * a)
    x2 = ((-1 * b) - math.sqrt(math.pow(b, 2) - (4 * a * c)))/(2 * a)
    print(f'El valor de X1 es: {x1:2f}')
    print(f'El valor de X2 es: {x2:2f}')