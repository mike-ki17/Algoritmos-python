import turtle
import math

def poligono(t, n, l):
    """Dibuja un polígono con n lados de longitud l."""
    for _ in range(n):
        t.forward(l)
        t.left(360 / n)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    poligono(t, n, length)

# Ejemplo de uso
t = turtle.Turtle()
radius = 100

circle(t, radius)

turtle.done()
