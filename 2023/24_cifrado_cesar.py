#  Crea un programa que realize el cifrado César de un texto y lo imprima.
#  También debe ser capaz de descifrarlo cuando así se lo indiquemos.

#  Te recomiendo que busques información para conocer en profundidad cómo
#  realizar el cifrado. Esto también forma parte del reto.

alfabeto_normal = 'abcdefghijklmnopqrstuvwxyz 1234567890'
alfabeto_cesar  = 'ghijklmnopqrstuvwxyz 1234567890abcdef'

print(alfabeto_cesar[alfabeto_normal.find('g')])
print(alfabeto_normal[alfabeto_cesar.find('m')])