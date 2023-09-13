'''
Escribir un programa en el cual Dados 5 números enteros solicitados al usuario, determinar cuál de los 4
números enteros es más cercano al primero.
'''

import math
valores = []

for i in range(5):
    valor = int(input(f'Ingrese el valor {i+1}: ').strip())
    valores.append(valor)

menor = [valores[0]]
cercano = []

for valor in valores[1:]:
    comparar = math.fabs(valores[0] - valor)

    for i in range(len(menor)):
        if comparar < menor[i]:
            menor[i] = comparar
            cercano.append(valor)
            break
        elif comparar == menor[i]:
            menor.append(comparar)
            cercano.append(valor)
            break

if len(cercano) > 1:
    print(f'Los valores mas cercanos a {valores[0]} son: {cercano}')
else:
    print(f'El valor mas cercano a {valores[0]} es: {cercano}')

