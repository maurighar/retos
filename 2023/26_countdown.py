# Crea una función que reciba dos parámetros para crear una cuenta atrás.
# - El primero, representa el número en el que comienza la cuenta.
# - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
# - Sólo se aceptan números enteros positivos.
# - El programa finaliza al llegar a cero.
# - Debes imprimir cada número de la cuenta atrás.

from time import sleep


def countdown(init:int, delay=1):
    if init < 0:
        print('El numero tiene que ser positivo')

    for number in range(init, -1, -1):
        sleep(delay)
        print(number)


if __name__ == "__main__":
    countdown(-1)
    countdown(3)
    countdown(3,2)
    