
'''Leer N números y calcular la media de los números pares y la media de los números impares, indicando en
cada caso las listas de cada tipo.'''


cantidadNums = int(input('Cantidad de números a calcular: '))


listPares = []
listImpares = []
for i in range(cantidadNums):
    n = int(input('Digita el número: '))
    if n % 2 == 0:
        listPares.append(n)
        mediaPares = sum(listPares)/(len(listPares))

    else :
        listImpares.append(n)
        mediaImpares = sum(listImpares)/(len(listImpares))

print(f'La media de los números pares es: {mediaPares}')
print(f'Lista números pares: {listPares}')
print(f'La media de los números impares es: {mediaImpares}')
print(f'Lista números impares: {listImpares}')
