''' Escribir un algoritmo para determinar el máximo común divisor de dos números enteros (MCD) por
el algoritmo de Euclides'''

def AlgoritmoEuclides (a, b):
  while not a % b == 0:
      c = b
      b = a % b
      a = c % b

  print(f'El MCD de los números es {c // b}')


AlgoritmoEuclides(100, 200)