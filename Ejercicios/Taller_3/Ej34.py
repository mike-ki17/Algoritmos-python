'''
 ¿Qué es un año bisiesto?
Un año bisiesto es un año dotado de un día adicional al término del mes de febrero (29 de febrero) y que
ocurre una vez cada cuatro años regulares. Este día “extra” reúne las fracciones de tiempo que sobran de los
cuatro años anteriores, dado que en el calendario tradicional un año consta de 365 días y no de los 365 días
con 5 horas 48 minutos y 45,10 segundos que establece el año solar o tropical calculado astronómicamente.
Cree un función que dé si un año es bisiesto o no, según:
Para determinar si un año es bisiesto, se deben considerar las siguientes reglas:
1) El año debe ser divisible por 4.
2) Si el año es divisible por 100, entonces también debe ser divisible por 400 para ser considerado bisiesto
'''

def is_year_leap(year):
    if year < 1582: leap = False
    elif year % 4 != 0: leap = False
    elif year % 100 != 0: leap = True
    elif year % 400 == 0: leap = True
    else: leap = False
    return leap


test_data = [1600,1900, 2000, 2016, 1987,2020,2024,2100]
test_results = [True,False, True, True, False,True,True,False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Fallido")    