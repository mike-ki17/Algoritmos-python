'''
22. Escriba un algoritmo con switch que indique:
W:Winter,SP:Spring,F:Fall,S:Summer
Y dé información sobre la duración de la estación correspondiente, por ejemplo si es W:
“Winter runs from December 1 to February 28”
'''

stations = {
    'W':['Winter', 'December 1 to February 28'],
    'SP':['Spting', 'March 20 to June 21'],
    'F': ['Fall', 'Septembebr 23 to December 21'], 
    'S': ['Summer', 'June 22 to September 23']
}

def statiosnSearch (station):
    s = stations.get(station, 'NA')
    return f'{s[0]} runs from {s[1]}'


print(statiosnSearch('SP'))