#  Crea un programa que realize el cifrado César de un texto y lo imprima.
#  También debe ser capaz de descifrarlo cuando así se lo indiquemos.

#  Te recomiendo que busques información para conocer en profundidad cómo
#  realizar el cifrado. Esto también forma parte del reto.

alfabeto_normal = 'abcdefghijklmnopqrstuvwxyz 1234567890'
alfabeto_cesar  = 'ghijklmnopqrstuvwxyz 1234567890abcdef'

# print(alfabeto_normal.find('t'))
# print(alfabeto_normal[alfabeto_cesar.find('m')])

def encode_cesar(message:str, shift:int) -> str:
    message = message.lower()
    message_cifer = ''
    for string in message:
        index = alfabeto_normal.find(string)
        if index >= 0:
            message_cifer += alfabeto_normal[index + shift]
        else:
            message_cifer += '#'

    return message_cifer

def decode_cesar(message:str, shift:int) -> str:
    message = message.lower()
    message_clear = ''
    for string in message:
        index = alfabeto_normal.find(string)
        if index >= 0:
            message_clear += alfabeto_normal[index - shift]
        else:
            message_clear += '#'

    return message_clear

def cifrado_cesar(texto, desplazamiento):
    # Generado chatGPT
    resultado = ""
    
    for caracter in texto:
        if caracter.isalpha():
            # Obtener el código ASCII del carácter y ajustar el desplazamiento
            codigo = ord(caracter) + desplazamiento
            
            # Si el código es mayor que el código ASCII de 'Z' o 'z',
            # volver al inicio del rango al restar 26 (número de letras en el alfabeto)
            if caracter.isupper() and codigo > ord('Z'):
                codigo -= 26
            elif caracter.islower() and codigo > ord('z'):
                codigo -= 26
            
            # Convertir el código ASCII de vuelta a carácter
            caracter_cifrado = chr(codigo)
            resultado += caracter_cifrado
        else:
            resultado += caracter
    
    return resultado

if __name__ == "__main__":
    mensaje = 'te recomiendo que busques informacion para conocer en profundidad'
    mensaje = 'prueba 234, si (?/7Ú\),\n MAYUSCULAS'
    print(encode_cesar(mensaje, 3))

    mensaje = 'wh3uhfrplhqgr3txh3exvtxhv3lqirupdflrq3sdud3frqrfhu3hq3surixqglgdg'
    # mensaje = 'suxhed3567#3vl3###0####3pd1xvfxodv'
    print(decode_cesar(mensaje, 3))
    print(cifrado_cesar(mensaje, -3))