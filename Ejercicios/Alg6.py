'''Escribir un algoritmo que calcule la suma de las potencias de un número hasta un valor n
especificado, según la fórmula.'''

n = int(input('Dame un número: '))
sumaTotal = 0
for i in range(10):
  sumaTotal += n**i

print(f'La sumatoria de las potencias del número {n} es: {sumaTotal}')