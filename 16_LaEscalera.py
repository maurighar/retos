# Crea una función que dibuje una escalera según su número de escalones.
# - Si el número es positivo, será ascendente de izquiera a derecha.
# - Si el número es negativo, será descendente de izquiera a derecha.
# - Si el número es cero, se dibujarán dos guiones bajos (__).

# Ejemplo: 4
#         _
#       _|
#     _|
#   _|
# _|

def escalera(niveles):
    print(niveles)
    stair = ''
    if niveles == 0:
        stair = '__'

    elif niveles > 0:
        for nivel in range(niveles):
            stair = '  '*(nivel) + '_|\r' + stair
        stair = '  '*(niveles)+'_\r' + stair

    else:
        stair += '_\r'
        for nivel in range(niveles*-1):
            stair += '  '*(nivel) + ' |_\r'
        stair += '  '*(niveles*-1)+' |_\r'
    print(stair)


if __name__ == '__main__':
    escalera(-8)
    escalera(6)
    escalera(0)