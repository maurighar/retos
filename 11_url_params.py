# Dada una URL con parámetros, crea una función que obtenga sus valores.
# No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#
# Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
# los parámetros serían ["2023", "0"]


def lee_param(url):
    params = [p for p in url.split('&')[1].split('=')]

    return params


if __name__ == '__main__':
    url = "https://retosdeprogramacion.com?year=2023&challenge=0"

    print(lee_param(url))
