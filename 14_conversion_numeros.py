'''
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.

 https://www.matesfacil.com/ESO/sistemas-numeracion/base-octal/sistema-numeracion-octal-base-ocho-ejemplos-teoria-propiedades-cambio-base-decimal-ejercicios-resueltos.html
'''

def convert_octa(numero: int, orden=1)-> int:
    resto = numero % 8
    cociente = int(abs(numero / 8))
    # print(resto, cociente)
    if cociente > 8:
        return convert_octa(cociente, orden*10)+resto*orden
    else:
        return resto*orden + cociente*orden*10


def hexa_caracter(num:int)-> str:
    match num:
        case 10:
            return 'A'
        case 11:
            return 'B'
        case 12:
            return 'C'
        case 13:
            return 'D'
        case 14:
            return 'E'
        case 15:
            return 'F'
        case _:
            return str(num)


def convert_hexa(numero: int)-> str:
    resto = numero % 16
    cociente = int(abs(numero / 16))

    if cociente > 16:
        return hexa_caracter(convert_hexa(cociente))+hexa_caracter(resto)
    else:
        return hexa_caracter(cociente) + hexa_caracter(resto)


if __name__ == '__main__':
    print(convert_hexa(460)) #1CC
    print(convert_hexa(1000)) #3E8
    print(convert_octa(768)) #1400
    print(convert_octa(1000)) #1750
    print(convert_octa(1235)) #2323
