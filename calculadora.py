# /*
#  * Lee el fichero "Challenge21.txt" incluido en el proyecto, calcula su
#  * resultado e imprímelo.
#  * - El .txt se corresponde con las entradas de una calculadora.
#  * - Cada línea tendrá un número o una operación representada por un
#  *   símbolo (alternando ambos).
#  * - Soporta números enteros y decimales.
#  * - Soporta las operaciones suma "+", resta "-", multiplicación "*"
#  *   y división "/".
#  * - El resultado se muestra al finalizar la lectura de la última
#  *   línea (si el .txt es correcto).
#  * - Si el formato del .txt no es correcto, se indicará que no se han
#  *   podido resolver las operaciones.
#  */  if isinstance (numero, int)

file_name = 'calculo.txt'

with open(file_name) as file:
	calculos = file.read()

for line in calculos.split():
	line = line
	if line in ['+','-']:
		pass
	else:
		print(line, int(line))

	# if int(line):
	# 	print(line)