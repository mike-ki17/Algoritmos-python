'''
20. Aplique una condición u operador Ternario para:
- Probar si una edad es menor de edad o mayor de edad.
- Probar M y F e indicar “Masculino” o “Femenino”.
- Probar dos veces (anidado) con operación ternaria M, F e indicar “Masculino” , “Femenino” o “No binario”.
'''


edad = 18
sexo = 'm'
mayorDeEdad = True if edad >= 18 else False
indicarSexo = 'Masculino' if sexo.upper() == 'M' else 'Femenino' if sexo.upper() == 'F' else 'No binario'

print(mayorDeEdad, indicarSexo)