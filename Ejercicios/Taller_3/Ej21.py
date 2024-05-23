'''
 21. Dar con un switch el Estado Civil segúnC (Casado), S (Soltero), U (Unión Libre), V (Viudo), D (Divorciado).
'''


estado_civil = {
    'C':'Casado',
    'S':'Soltero',
    'U':'Union Libre',
    'V':'Viudo',
    'D':'Divorciado'
}

def EstadoCivil(estado):
    return estado_civil.get(estado, "NA")

print(EstadoCivil('U'))