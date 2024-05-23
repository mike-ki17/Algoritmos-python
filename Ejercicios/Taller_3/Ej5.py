import turtle

def dibujar_figura(tipo_figura, longitud_lado, longitud_lado2=None):
    t = turtle.Turtle()

    if tipo_figura == 'triangulo':
        for _ in range(3):
            t.forward(longitud_lado)
            t.left(120)
    elif tipo_figura == 'cuadrado':
        for _ in range(4):
            t.forward(longitud_lado)
            t.left(90)
    elif tipo_figura == 'rectangulo':
        if longitud_lado2 is None:
            print("Para un rectángulo, debe proporcionar la longitud de los dos lados.")
            return
        for _ in range(2):
            t.forward(longitud_lado)
            t.left(90)
            t.forward(longitud_lado2)
            t.left(90)
    else:
        print("Tipo de figura no reconocido. Utilice 'triangulo', 'cuadrado' o 'rectangulo'.")

    turtle.done()

# Ejemplo de uso
dibujar_figura('triangulo', 100)
# dibujar_figura('cuadrado', 100)
# dibujar_figura('rectangulo', 100, 50)
