# Crea un programa que analice texto y obtenga:
# - Número total de palabras.
# - Longitud media de las palabras.
# - Número de oraciones del texto (cada vez que aparecen un punto).
# - Encuentre la palabra más larga.
# Todo esto utilizando un único bucle.


def main(texto:str):
  palabras = texto.split(' ')
  oraciones = texto.split('.')
  print(len(palabras))
  print(oraciones)
  print(len(oraciones))


if __name__ == '__main__':

  textoOriginal = '''En estos tiempos en los que pasamos gran parte de nuestras vidas en línea, es más importante que nunca mantener nuestra información personal y nuestras cuentas de redes sociales seguras. Y hablando de redes sociales, Instagram hace todo lo posible para mantener la seguridad de sus usuarios. Sin embargo, nunca se sabe quién puede estar tratando de acceder a tu cuenta sin tu conocimiento. Por suerte, hay maneras de detectar si alguien ha entrado en tu cuenta de Instagram sin tu permiso. A continuación, te mostramos cómo hacerlo. Instagram te permite ver todas las actividades recientes en tu cuenta. Desde el menú principal, dirígete a tu perfil y toca el icono de las tres líneas en la esquina superior derecha. Luego, ingresa en Configuración y, en la parte inferior, accede a la opción de Actividad de inicio de sesión.'''

  textoCorto = 'En estos tiempos en los que pasamos gran parte. de nuestras vidas en línea.'

  main(textoCorto)