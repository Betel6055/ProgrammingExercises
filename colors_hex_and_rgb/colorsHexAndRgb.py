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

while True:
    try:
        rgb = input('Enter the color rgb in format (r,g,b): ')
        r, g, b = map(int, rgb.split(','))
        assert 0 <= r <= 255, 'The value for r must be between 0 and 255'
        assert 0 <= g <= 255, 'The value for g must be between 0 and 255'
        assert 0 <= b <= 255, 'The value for b must be between 0 and 255'
        break
    except ValueError as ve:
        print(f'Error: {ve}')
        print('You must enter 3 values separated by commas')
    except Exception as e:
        print(f'Error: {e}')

while True:
    try:
        hex_ = input('Enter the value hexadecimal in format (#000000): ')
        assert len(hex_) == 7, 'The value does not contain the number of strings required'
        break
    except Exception as e:
        print(f'Error: {e}')

print(rgbToHex(r, g, b))
print(hexToRgb(hex_))
