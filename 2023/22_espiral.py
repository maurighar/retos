#  Crea una función que dibuje una espiral como la del ejemplo.
#  - Únicamente se indica de forma dinámica el tamaño del lado.
#  - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
# 
#  Ejemplo espiral de lado 5 (5 filas y 5 columnas):
#  ════╗
#  ╔══╗║
#  ║╔╗║║
#  ║╚═╝║
#  ╚═══╝

def espiral(tamano):
    dibujo = ''
    for alto in range(1, tamano+1):
        if alto == 1:
            dibujo += f'═'
        else:
            dibujo += f'║'
        
    print(dibujo)
    
    
def draw_spiral(size):
    pass
    
if __name__ == '__main__':
    espiral(6)
    