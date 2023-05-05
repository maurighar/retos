'''
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.

 https://www.matesfacil.com/ESO/sistemas-numeracion/base-octal/sistema-numeracion-octal-base-ocho-ejemplos-teoria-propiedades-cambio-base-decimal-ejercicios-resueltos.html
'''

def convert_octa(numero: int, orden=1)-> int:
    resto = numero % 8
    cociente = numero // 8
    # print(resto, cociente)
    if cociente > 8:
        return convert_octa(cociente, orden*10)+resto*orden
    else:
        return resto*orden + cociente*orden*10


def convert_hexa(numero: int)-> str:
    hex_values = "0123456789ABCDEF"

    resto = numero % 16
    cociente = numero // 16

    if cociente > 16:
        return convert_hexa(cociente)+hex_values[resto]
    else:
        return hex_values[cociente] + hex_values[resto]


if __name__ == '__main__':
    print(convert_hexa(460)) #1CC
    print(convert_hexa(1000)) #3E8
    print(convert_octa(768)) #1400
    print(convert_octa(1000)) #1750
    print(convert_octa(1235)) #2323
