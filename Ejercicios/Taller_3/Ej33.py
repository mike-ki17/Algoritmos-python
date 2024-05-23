'''
33. Escribe una función llamada identidad(n) que cree una matriz cuadrada de identidad, que es una matriz
cuyos elementos son 0, excepto los elementos de la diagonal (desde arriba a la izquierda hasta abajo a la
derecha) que tienen un valor de 1. La diagonal está formada por aquellos elementos cuyas posiciones en la
matriz de fila y columna son iguales:
(1,1), (2,2), etc. La función toma un argumento de entrada entero positivo, que es el tamaño de la matriz, y
devuelve la propia matriz como argumento de salida. Por ejemplo, identity(4) debe devolver una matriz
identidad de 4 por 4:
1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
'''
import numpy as np

def identidad (n):
    matriz_identidad = np.array([1  if row == column else 0 for row in range(n) for column in range(n)]).reshape(n,n)

    return matriz_identidad
print(identidad(4))


# def identidad(n):
#     m = []
#     for row in range(n):
#         for colum in range(n):
#             if row == colum:
#                 m.append(1)
#             else:
#                 m.append(0)
        
#     m = np.array(m).reshape(n,n)
#     return m


# print(identidad(8))