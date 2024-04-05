

def convertInt(n, base):
    condicion = True
    listaConvertida = []
    numeroResultante = ''
    while condicion:
        b = n % base
        n = n // base
        listaConvertida.append(b)
        if (n == 1 or n == 0) or ((base == 8 or base == 16) and n < base):
            listaConvertida.append(n)
            listaConvertida = listaConvertida[::-1]
            condicion = False
    for i in listaConvertida:
        a = str(i)
        numeroResultante += a
    return int(numeroResultante)


print(f'El numero es: {convertInt(10, 2)}')

