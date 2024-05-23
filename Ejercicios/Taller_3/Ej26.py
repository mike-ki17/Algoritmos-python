'''
26. Escriba una función llamada luz_tiempo que tome como entrada un vector fila de distancias en millas y
devuelve dos vectores fila de la misma longitud. Cada elemento del primer argumento de salida es el tiempo en
minutos que la luz tardaría en recorrer la distancia especificada por el elemento correspondiente del vector de
entrada. Para comprobar sus cálculos, la luz solar tarda algo más de 8 minutos en llegar a Tierra que está a 92,9
millones de millas. La segunda salida contiene las distancias de entrada convertidas a kilómetros. Supongamos
que la velocidad de la luz es de 300.000 km/s y que una milla equivale a 1,609 km.
'''


def luz_tiempo (distancias):

    # Se utiliza la formula de la velocidad para calcular el tiempo
    # Primero se convierte la distancia de millas a kilometros la dividimos con la velocidad luz y dividimos en 60 para tener un resultado en minutos
    tiempos = [f'{round(((distancias[i]*1.60934) / 300000)/60, 2)} minutos' for i in range(len(distancias))]
    # Se crea un vector que tendra las distancias pasadas de millas a kilometros
    distancias_km = [f'{round(distancias[i]*1.60934, 1)} km' for i in range(len(distancias))]

    return (tiempos, distancias_km)


millas = [92000000.9]

print(luz_tiempo(millas))