
from turtle import *



def Piramides (numeroCuadrados, longitud):

   for i in range(numeroCuadrados):
       for i in range(4):
        forward(longitud)
        left(90)
       longitud -= 8 # este valor puede variar
       left(45)
       forward(10) # Este valor puede variar
       right(45)
    
   

   

Piramides(20, 200)


end_fill()
done()