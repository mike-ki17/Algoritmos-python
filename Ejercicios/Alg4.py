'''Hallar factorial de número solicitado'''


n = int(input('Ingresa el número para hallar su factorial: '))

factorial = 1
for i in range(n):
    factorial *= n-i

print(f'El factorial del número {n} es {factorial}')