'''
29. Escriba una función llamada matrizH que tome un vector fila v como entrada y devuelva una matriz H cuya
primera columna consiste en los elementos de v, cuya segunda columna consiste en los cuadrados de los
elementos de v, y cuya tercera columna consiste en los cubos de los elementos v. Por ejemplo, si se
llama a la función así, A = matrizH(1:3) , entonces A será {{ 1 1 1},{2 4 8},{ 3 9 27}}.
'''



import numpy as np

def matrizH(v):

    m = np.array([[i, i**2, i**3] for i in range(1, v+1)]).reshape(v,3)
    return m

print(matrizH(3))