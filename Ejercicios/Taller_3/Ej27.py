'''
27. Escribe una función llamada pita que toma una matriz llamada ab como argumento de entrada. La matriz
ab tiene exactamente dos columnas. La función debe devolver un vector de columnas c que contenga valores
positivos cada uno de los cuales satisface el Teorema de Pitágoras, para la fila correspondiente de ab
suponiendo que los dos elementos de cada fila de ab corresponden a un par, a y b respectivamente, en el
teorema. Tenga en cuenta que la función incorporada de MATLAB sqrt calcula la raíz cuadrada raíz cuadrada y
puede utilizarla.
'''
import numpy as np

pita = lambda vectores: np.array([round(np.sqrt(i[0]**2 + i[1]**2),2) for i in vectores]).reshape(-1,1)

ab = [[3,4],[5,6]]

print(pita(ab))