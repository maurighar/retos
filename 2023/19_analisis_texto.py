# Crea un programa que analice texto y obtenga:
# - Número total de palabras.
# - Longitud media de las palabras.
# - Número de oraciones del texto (cada vez que aparecen un punto).
# - Encuentre la palabra más larga.
# Todo esto utilizando un único bucle.

import re

def main(texto:str):
  palabras = texto.replace("\n", " ").split(" ")
  
  words_count = 0
  oraciones_count = 0
  letras_count = 0
  palabra_larga = ''
  
  for palabra in palabras:
    
    if len(palabra) == 0:
      continue
    
    print(palabra)
    
    if '.' in palabra:
      oraciones_count += 1
    
    palabra_actual = re.sub(r"[^\w]", "", palabra)
    
    letras_count += len(palabra_actual)
    words_count += 1
    palabra_larga = palabra if len(palabra_actual) >= len(palabra_larga) else palabra_larga
  
  print(f'Oraciones: {oraciones_count}')
  print(f'Palabra larga: {palabra_larga}')
  print(f'Cantidad palabrar: {words_count}')
  print(f'Longitud promedio: {letras_count/words_count}')


if __name__ == '__main__':

  textoOriginal = """
Nos encontramos en un
periodo de guerra civil. Las
naves espaciales rebeldes,
atacando desde una base
oculta, han logrado su
primera victoria contra
el malvado Imperio
Galáctico.

Durante la batalla, los
espías rebeldes han
conseguido apoderarse de
los planos secretos del
arma total y definitiva del
Imperio, la ESTRELLA
DE LA MUERTE,
una estación espacial
acorazada, llevando en sí
potencia suficiente para
destruir a un planeta
entero.

Perseguida por los
siniestros agentes del
Imperio, la Princesa Leia
vuela hacia su patria, a
bordo de su nave espacial,
llevando consigo los
planos robados, que
pueden salvar a su pueblo
y devolver la libertad a la
galaxia....
"""

  main(textoOriginal)
