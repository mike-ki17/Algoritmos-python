'''Escriba un algoritmo que encuentre el salario semanal de un trabajador por horas, dada la tarifa
horaria y el número de horas trabajadas diariamente.'''

print('Salario semanal')
tarifaHoraria = 5000
salarioSemanal = 0
n = 1
while n <= 7:
    h = int(input(f'Horas trabajadas el día {n}: ' ))
    salarioSemanal += h
    n+=1
_salarioSemanal_ = salarioSemanal * tarifaHoraria

print(f'El salario semanal del trabajador es: {_salarioSemanal_}')