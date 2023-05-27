# Crea un programa que encuentre y muestre todos los pares de números primos
# gemelos en un rango concreto.
# El programa recibirá el rango máximo como número entero positivo.
# 
# - Un par de números primos se considera gemelo si la diferencia entre
  # ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
# - Ejemplo: Rango 14
  # (3, 5), (5, 7), (11, 13)


def is_prime(n:int)->bool:
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def main(ranges:int) -> tuple:
  prime_twins = []
  
  for number in range(1,ranges+1):
    if is_prime(number) and is_prime(number+2):
      prime_twins.append((number,number+2))
  return prime_twins


if __name__ == '__main__':
  print(main(60))
