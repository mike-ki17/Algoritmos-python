
'''Escriba un algoritmo que calcule el promedio geométrico de n números'''


cantidad = int(input('Ingresa la cantidad de números a evaluar: '))
promedio = 1
for i in range(1, cantidad + 1):
    if not i == 5:
        n = int(input('Ingresa un número: '))
        promedio *= n 
        _promedio_ = promedio ** (1/i)
        print(f'El promedio geometrico de los numeros ingresados es: {_promedio_}')
    else:
        state = False
