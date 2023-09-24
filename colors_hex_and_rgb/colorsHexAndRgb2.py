"""
/*
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
 */
"""

def rgbToHex(r = 0, g = 0, b = 0) -> hex:
    hex_ = "#{:X}{:X}{:X}".format(r, g, b)
    return hex_

def hexToRgb(hex_) -> tuple:
    r, g, b = int(hex_[1:3], 16), int(hex_[3:5], 16), int(hex_[5:7], 16)
    rgb = (r, g, b)
    return rgb

print(rgbToHex(255, 255, 255))
print(hexToRgb('#7250AB'))
