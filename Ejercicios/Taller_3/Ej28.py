'''
28. Escribe una función llamada abajo_izquierda que tome dos entradas: una matriz N y un escalar n, en ese
orden, donde cada dimensión de N es mayor o igual que n. La función devuelve la matriz cuadrada n por n
en la esquina inferior izquierda de N
'''

import numpy as np



def abajo_izquierda (m, n):

    longitudArray = len(m)-1
    matriz_recortada = np.array([m[longitudArray-i][x] for i in range(n-1, -1, -1) for x in range(0,n)]).reshape(n,n)

    return matriz_recortada




m = np.array([[4, 7, 10, 6],
              [2, -5, 3, 8],
              [8, 9, 1, 0],
              [5, 4, 1, 0],
              [8, 9, 1, 0]])


print(abajo_izquierda(m, 3))




'''
# longitudArray = len(m)-1
# indexs = [m[index-1][0], m[index-1][1], m[index][0], m[index][1]]

# for i in range(n-1, -1, -1):
#     for x in range(0,n):
#         print(m[longitudArray-i][x])

'''