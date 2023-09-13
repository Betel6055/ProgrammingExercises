"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below N.

Input Format

First line contains T that denotes the number of test cases. This is followed by T lines, each containing an integer, N.

Constraints
* 1 <= T <= 10^5
* 1 <= N <= 10^9

Output Format

For each test case, print an integer that denotes the sum of all the multiples of 3 or 5 below N.

Sample Input 0

2
10
100
Sample Output 0

23
2318
Explanation 0

For N = 10, if we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Similarly for N = 100, we get 2318.
"""

# !/bin/python3

import math
import os
import random
import re
import sys
import time
from numba import njit


if __name__ == '__main__':
    t = int(input().strip())
    @njit()
    def sumar(n):
        if 1 <= n <= math.pow(10, 9):
            lista_numeros = 0
            for numero in range(1, n):
                if numero % 3 == 0 or numero % 5 == 0:
                    lista_numeros += numero
        return lista_numeros

    if 1 <= t <= math.pow(10, 5):
        for t in range(t):
            # n = int(input().strip())
            # n = random.randint(1, 1000000000)
            n = 1000000000
            print(n)
            inicio = time.time()
            resultado = sumar(n)
            fin = time.time()
            print(f'{n}: {resultado}')
            print(f'La operacion se demoro: {(fin - inicio)}')