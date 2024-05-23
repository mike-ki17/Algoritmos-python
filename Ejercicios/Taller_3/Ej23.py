'''
23. Escriba una función llamada posicion_impar que tome una matriz, M, como argumento de entrada y
devuelva una matriz que contiene sólo aquellos elementos de M que están en filas y columnas impares. En
otras palabras, devolvería los elementos de M en las posiciones (1,1), (1,3), (1,5), ..., (3,1), (3,3), (3,5), ..., etc.
Tenga en cuenta que tanto la fila y la columna de un elemento deben ser impares para ser incluidos en la
salida. Por ejemplo, si M fuera una matriz de 5 por 8, entonces la salida debe ser de 3 por 4 porque la función
omite las filas 2 y 4 de M y también omite las columnas 2, 4, 6 y 8 de M.
'''
import numpy as np

# Creamos la funcion 'posicion_impar' la cual recibe una matriz
def posicion_impar(m):
    # Primero creamos un arreglo con todas las posiciones impares, vasandose en tomar todos los indices impares de cada fila 
    rows = [[row, item] for row in range(len(m)) for item in range(len(m[0])) if (row % 2 == 0 or row == 0) and (item % 2 == 0)]
    # Por consiguiente creamos una nueva matriz la cual agrega los elementos de la matriz de entrada, pero solo de las posiciones del arreglo 'rows' 
    m_impar = np.array([m[index[0]][index[1]] for index in rows])
    # Finalmente redimencionamos la matriz creada anteriormente 
    m_impar = np.reshape(m_impar, ((len(m)//2 if len(m) % 2 == 0 else len(m)//2 + 1), (len(m[0])//2)))

    return m_impar


# Matriz de entrada
m = np.array([[3, 4, 5, 6, 7, 3, 4, 5], 
              [1, 2, 3, 6, 7, 3, 4, 5], 
              [1, 1, 3, 9, 7, 3, 4, 5], 
              [4, 6, 7, 3, 4, 3, 4, 5], 
              [3, 4, 5, 8, 9, 3, 4, 5]])

print(posicion_impar(m))






'''
# #m_impar = np.vstack(m[1::2]) # Apilas las filas impares verticalmente formando una nueva matriz 
# #print(m_impar)

# m_impar = np.array([])
# rows = []

# for row in range(len(m)):
#     for item in range(len(m[0])):
#         if (row % 2 == 0 or row == 0) and (item % 2 == 0):
#             rows.append([row, item])
'''