'''Escriba un algoritmo que calcule el promedio aritmético de n números, ingresando primero n y
luego los números, según:'''

n = int(input('Cantidad de numeros a evaluar: '))
promedioAritmetico = 0
for i in range(1,n+1):
    x = int(input(f'Ingresa el numero {i}: '))
    promedioAritmetico += x
    _promedioAritmetico_ = promedioAritmetico / n

print(f'El promedio aritmetico de los numeros ingresados es {_promedioAritmetico_}')



