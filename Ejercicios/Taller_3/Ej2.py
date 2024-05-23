

from turtle import *


def poligono(nombre, numeroLados, longitud):
    angle = 360 / numeroLados
    for i in range(numeroLados):
        forward(longitud)
        left(angle)


poligono('Octagono', 8, 50)

end_fill()
done()