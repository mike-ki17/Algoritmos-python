'''7. Elaborar una función que le reporte al electricista de un edificio recién construido cuantos bombillos debe
comprar. Se sabe que el edificio tiene 8 pisos, 8 apartamento en cada piso y cada apartamento tiene 8
bombillos. En la solución se debe emplear una estructura repetitiva. Luego la función debe generalizar a
cualquier edificio con x pisos, y apartamentos y z bombillos por apartamento.'''



def cantidadBombillos(pisos, apartamentos, bombillos):
    totalBombillos = 0
    for piso in range(pisos):
        for apartamento in range(apartamentos):
            for bombillo in range(bombillos):
                totalBombillos += 1
    
    print(f'EL edificio tiene un total de {totalBombillos} bombillos')    


cantidadBombillos(8,8,8)