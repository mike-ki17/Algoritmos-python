
'''Diseñar un algoritmo que imprima y sume la serie de números 3, 6, 9, 12…, 99.'''


sumaDeLaSerieDeNumeroDivisiblesPorTres = 0
for i in range(3, 100, 3):
  print(i)
  sumaDeLaSerieDeNumeroDivisiblesPorTres += i

print(f'La sumatoria de los numeros de la serie del 3 es: {sumaDeLaSerieDeNumeroDivisiblesPorTres}')