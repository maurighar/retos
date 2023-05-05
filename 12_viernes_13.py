 # Crea una función que sea capaz de detectar si existe un viernes 13
 # en el mes y el año indicados.
 # - La función recibirá el mes y el año y retornará verdadero o falso.
from datetime import date

def viernes_13(mes=1, anno=2023):
    if 1 <= mes <= 12:
        dia = date(anno,mes,13)

        return dia.weekday() == 4
    else:
        print('El mes debe ser entre 1 y 12.')
        return False


if __name__ == '__main__':
    print(viernes_13(12,2023))
    print(viernes_13(10,2023))
