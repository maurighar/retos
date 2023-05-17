#  ¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible!
# Crea un programa que dibuje una Trifuerza de "Zelda"
# formada por asteriscos.
# - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
# - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
# Ejemplo: Trifuerza 2

#    *
#   ***
#  *   *
# *** ***

def trifuerza(filas:int)->None:
    for nivel in range(1,filas+1):
        print(' '*(filas*2-nivel) + '*'*(2 * nivel-1))

    for nivel in range(1,filas+1):
        print(' '*(filas-nivel) + '*'*(2 * nivel-1) + ' ' * (filas-nivel) + ' '*(filas-nivel+1) + '*'*(2 * nivel-1))

if __name__ == '__main__':
    trifuerza(4)