"""
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
"""
import string

def excel_col(column:str)->int:
    alphabet = list(string.ascii_uppercase)
    value_columns = 0

    for letter in column.upper():
        value_columns = (value_columns * len(alphabet)) + (alphabet.index(letter) +1 )

    return value_columns



if __name__ == '__main__':
    print(excel_col('AA')) # 27
    print(excel_col('CA')) # 79