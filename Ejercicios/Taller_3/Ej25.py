'''
25. Supongamos que tenemos un montón de monedas. Escribe una función llamada rica que calcule cuánto
dinero tenemos. Toma un argumento de entrada que es un vector de filas cuyos 4 elementos especifican el
número de monedas pennies (1 centavo), nickels (5 centavos), dimes (10 centavos) y quarters (25 centavos)
que tenemos (en el orden indicado aquí). La salida de la función es el valor del total en dólares (no en
centavos). En ejemplo, si tuviéramos cinco monedas, cuatro quarters y un pennie, la respuesta sería 1,01
dólares.
'''


def Dollars (monedas):
   
    values_coins = [1, 5, 10, 25]

    centavos = 0
    # for i in range(len(monedas)):
    #     centavos += (monedas[i] * values_coins[i])
    [centavos :=  centavos + (monedas[i] * values_coins[i]) for i in range(len(monedas))]

    return f'Tienes un total de US$ {(centavos / 100)} dolares'
 

monedas = [1,0,0,4]
print(Dollars(monedas))

