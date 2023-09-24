"""
/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */
"""

def rgbToHex(r = 0, g = 0, b = 0):
    r_quotient = []
    r_remainder = []
    while True:
        if len(r_quotient) > 0 and r_quotient[-1] > 16:
            quotient = r_quotient[-1] // 16
            remainder = r_quotient[-1] % 16
            r_quotient.append(quotient)
            r_remainder.append(remainder)
        elif len(r_quotient) == 0:
            quotient = r // 16
            remainder = r % 16
            r_quotient.append(quotient)
            r_remainder.append(remainder)
        else:
            quotient = r_quotient[-1]
            r_remainder.append(quotient)
            break

    print(r_quotient)
    print(r_remainder)

rgbToHex(7000, 0, 0)
# print(7000 % 16)
# print(7000 / 16)
# print(7000 // 16)