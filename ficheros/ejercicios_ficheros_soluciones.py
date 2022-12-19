#Lee el fichero 'ejercicio1.csv' de la forma que consideres. Muestra por pantalla la información que aparece en cada línea


import csv
with open('ejercicio1.csv',encoding='utf8') as f:
    data = csv.reader(f,delimiter=';')
    contador=0
    for line in data:
        if contador==0:
            contador+=1
            continue
        print(' '.join(line))



# Guarda los datos de cada línea en un diccionario distinto donde las claves son las cabeceras del csv y a su vez,
# guarda los diccionarios en una lista de diccionarios.
# Almacena esta información en un fichero pickle o json (el que quieras) llamado 'ejercicio2'. Ejemplo:
# 2,Javier,Mendoza,21/02/02 pasaría a ser {index:2,name:Javier,surname:Mendoza,date:21/02/02}

dictionaries = []
with open('ejercicio1.csv',mode='r',encoding='utf8') as f:
    data = csv.reader(f,delimiter=';')
    contador=0
    for line in data:
        if contador==0:
            cabeceras = line
            contador+=1
            continue
        dictionary = {}
        for i in range(len(line)):
            dictionary[cabeceras[i]]=line[i]
        dictionaries.append(dictionary)

import json
with open('ejercicio2.json',mode='w',encoding='utf8') as f:
    json.dump(dictionaries,f)


#Carga el fichero ejercicio3.pickle que contiene una lista de coches.
#Cambiar la posición de uno de ellos de forma persistente.
import pickle
class Coche:
    ruedas = 4
    def __init__(self,marca,plazas,matricula,color,precio,tags=[]):
        self.marca = marca
        self.plazas = plazas
        self.matricula = matricula
        self.color = color
        self.precio = precio
        self.tags = tags
        self.position = (0,0)
        self.cuentakm = 0
    def teletransportar(self,x,y):
        self.position = (x,y)
    def drive(self,num):
        self.cuentakm+=num

with open('ejercicio3.pickle',mode='rb') as f:
    coches = pickle.load(f)

print(coches[0].position)
coches[0].teletransportar(10,9)

with open('ejercicio3.pickle',mode='wb') as f:
    pickle.dump(coches,f)

