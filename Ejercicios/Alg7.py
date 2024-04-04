'''Escribir un algoritmo que calcule la suma de los cuadrados de los primeros n números'''

n2 = int(input('Dame un número: '))
sumaTotalCuadrados = 0

for i in range(1,n2+1):
  sumaTotalCuadrados += i**2

print(f'La sumatoria de los cuadrados de los números hasta {n2} es {sumaTotalCuadrados}')