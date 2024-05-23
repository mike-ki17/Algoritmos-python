'''
24. Escribe una función llamada int_col que tenga un argumento de entrada, un entero positivo n que sea
mayor que 1, y un argumento de salida v que es un vector columna de longitud n que contiene todos los
enteros positivos menores o iguales que n, ordenados de tal manera que ningún elemento del vector sea igual
a su propia posición. En otras palabras, v(k) no es igual a k para ninguna posición válida k.
'''
import numpy as np

def int_col (n):
    if n >= 1:
        # Se crea una lista de los enteros positivos menores e iguales a n
        list_nums = [i for i in range(1,n+1)]
        # En caso de que 'n' sea par invertiremos el orden del arreglo de numeros anterior
        if n % 2 == 0:
            v = np.array([index for index in range(len(list_nums), 0, -1)]).reshape(-1, 1)
        # En caso de que 'n' sea impar se hace lo mismo pero moviendo el elemento central a la ultima posición
        else:
            v = np.array([index for index in range(len(list_nums), 0, -1)])
            v = np.delete(v, (n//2))
            v = np.append(v, list_nums[(n//2)]).reshape(-1, 1)
    
    return v


print(int_col(5))