


# n = int(input('Ingresa el número para hallar su factorial: '))
# factorial = 1
# i = 1
# while i < n+1:
#     factorial *= i
#     i+=1
# print(f'El factorial del número {n} es: {factorial}')



# promedioAritmetico = 0
# for i in range(1,n+1):
#     x = int(input(f'Ingresa el numero {i}: '))
#     promedioAritmetico += x
#     _promedioAritmetico_ = promedioAritmetico / n

# print(f'El promedio aritmetico de los numeros ingresados es {_promedioAritmetico_}')

print('========== Para detener el programa digite el número 99 ==============')
print('============== Digita los salarios de los empleados ==================')
status = True
promedio = 0
count = 0
while status:
    n = int(input('< Ingresa los salarios: '))
    if not n == 99:
        promedio += n
    else:
        promedio = promedio / count
        print(f'El promedio dde la nomina de los salarios es : ${promedio}')
        status = False
    
    count += 1






