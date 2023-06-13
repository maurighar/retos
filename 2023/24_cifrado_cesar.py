#  Crea un programa que realize el cifrado César de un texto y lo imprima.
#  También debe ser capaz de descifrarlo cuando así se lo indiquemos.

#  Te recomiendo que busques información para conocer en profundidad cómo
#  realizar el cifrado. Esto también forma parte del reto.

alfabeto_normal = 'abcdefghijklmnopqrstuvwxyz 1234567890'
alfabeto_cesar  = 'ghijklmnopqrstuvwxyz 1234567890abcdef'

# print(alfabeto_normal.find('t'))
# print(alfabeto_normal[alfabeto_cesar.find('m')])

def encode_cesar(message:str) -> str:
    message = message.lower()
    message_cifer = ''
    for string in message:
        index = alfabeto_normal.find(string)
        if index >= 0:
            message_cifer += alfabeto_cesar[index]
        else:
            message_cifer += '#'

    return message_cifer

def decode_cesar(message:str) -> str:
    message = message.lower()
    message_clear = ''
    for string in message:
        index = alfabeto_cesar.find(string)
        if index >= 0:
            message_clear += alfabeto_normal[index]
        else:
            message_clear += '#'

    return message_clear

if __name__ == "__main__":
    print(encode_cesar('te recomiendo que busques informacion para conocer en profundidad'))

    print(decode_cesar('zk6xkiusoktju6w k6h yw ky6otluxsgiout6vgxg6iutuikx6kt6vxul tjojgj'))