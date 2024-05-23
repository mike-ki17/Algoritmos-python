'''
30. Escriba una función convTemp(T,Tipo), que pida como parámetros T una Temperatura y en Tipo un carácter
según:
- “C” o “c” para grados Celsius
- “F” o “f” para grados Fahrenheit
- “K” o “k” para Kelvin
- “R” o “r” para Rankine.
La función debe retornar todas las otras tres equivalencias a la temperatura ingresada y se debe imprimir los
resultados en forma de tabla, así, si se ingresó 100 y “c”, debe arrojar:
----------------------------------------
C    F   K      R
100 212 373.15 671.7
----------------------------------------
'''

def convTemp(t, tipo):
    temp = []
    if tipo == 'C':
        temp.append(t)
        temp.append(round((t*9/5)+32))
        temp.append(round(t+273.15))
        temp.append(round((t + 273.15)*9/5))
    elif tipo == 'F':
        temp.append(round((t *32)*5/9))
        temp.append(t)
        temp.append((round(t+459.67)*5/9))
        temp.append(round(t + 459.67))
    elif tipo == 'K':
        temp.append(round(t-273.15))
        temp.append(round((t * 9/5)-459.67))
        temp.append(t)
        temp.append(round(t * 9/5))
    elif tipo == 'R':
        temp.append(round((t-491.67)*5/9))
        temp.append(round(t-459.67))
        temp.append(t*5/9)
        temp.append(t)
    
    
    print(f'---------------------------------------- \n C    F     K    R  \n{temp[0]}  {temp[1]}  {temp[2]}   {temp[3]} \n----------------------------------------')


convTemp(100, 'R')