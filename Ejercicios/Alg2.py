'''Algoritmo para encontrar la sucesión de Fibonacci hasta un No. Dado.'''


print('Secuencia de Fibonacci')
n = int(input('Hasta que número quiere que llegue la secuencia: '))
actual = 1
nuevo = 0
for i in range(n):
    nuevo = actual + nuevo
    actual = nuevo - actual
    print(nuevo, end=", ")

