#  Crea una función que reciba dos cadenas de texto casi iguales,
#  a excepción de uno o varios caracteres. 
#  La función debe encontrarlos y retornarlos en formato lista/array.
#  - Ambas cadenas de texto deben ser iguales en longitud.
#  - Las cadenas de texto son iguales elemento a elemento.
#  - No se pueden utilizar operaciones propias del lenguaje
#    que lo resuelvan directamente.
#  
#  Ejemplos:
#  - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
#  - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]

def infiltred_char(str_base:str, str_compare:str)->list():
    result = []
    for index in range(len(str_base)):
        if str_base[index] !=  str_compare[index]:
            result.append( str_compare[index])

    return result

def infiltred_char2(str_base:str, str_compare:str)->list():
    indexs = range(len(str_base))
    result = [str_compare[index] for index in indexs if str_base[index] !=  str_compare[index]]

    return result
    

if __name__ == "__main__":

    cadena1 = 'Me llamo mouredev'
    cadena2 = 'Me llemo mouredov'

    print(infiltred_char(cadena1,cadena2))
    print(infiltred_char2(cadena1,cadena2))
