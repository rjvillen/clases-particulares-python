#SIEMPRE SIEMPRE SIEMPRE que abrimos un fichero lo tenemos que CERRAR después
#Si abrimos un fichero con with, python hace el close() por nosotros :))

fichero = 'nombres2.txt' #qué tengo que poner como fichero?
            #qué pasa si no está en la misma carpeta?

import pickle
import csv

with open(fichero) as f:
    print(f) #qué imprime?

with open(fichero) as f: #qué ha pasado?
    print(f.read())

with open(fichero,encoding='utf8') as f: #qué ha pasado?
    print(f.read())

with open(fichero,encoding='utf8') as f: #por qué sale así? cómo podemos solucionarlo?
    for line in f:
        print(line.strip())

with open(fichero,encoding='utf8') as f:
    lines=f.readlines() #lines=[Rocío,Ana...]
    for l in lines:
        print(l)

with open(fichero,mode='a',encoding='utf8') as f:
    f.write('\nIrene') #probar primero sin \n

lista=[1,2,3,4]
with open('lista.pickle',mode='wb') as f:
    pickle.dump(lista, f)

with open('lista.pickle',mode='rb') as f:
    print(pickle.load(f))

with open('lista.pickle',mode='rb') as f:
    x = pickle.load(f)
    x[0]=9
with open('lista.pickle',mode='wb') as f:
    pickle.dump(x,f)
with open('lista.pickle',mode='rb') as f:
    print(pickle.load(f))



import csv

with open('personas.csv', mode='r') as fichero:
    csv_reader = csv.reader(fichero, delimiter=',')#guardamos las líneas del fichero en csv_reader
    contador = 0
    for linea in csv_reader:#¿qué es una línea en un csv?

        if contador == 0:
            cabeceras = linea
            contador += 1
            
        else:
            print('Línea ' + str(contador) + ':')
            
        for i in range(len(cabeceras)):
            print(cabeceras[i], '->', linea[i])
            contador += 1

with open('personas.csv', mode='a', encoding='utf8', newline='') as fichero:
    csv_writer = csv.writer(fichero, delimiter=',')
    linea = ['Pablo','Buendía','24']
    csv_writer.writerow(linea)
    linea = ['Enrique', None,'15']
    csv_writer.writerow(linea)



import json
diccionario = {
    'nombre':'Marta',
    'edad':25
}

with open('diccionario.json',mode='w',encoding='utf8') as f:
    json.dump(diccionario,f)

with open('diccionario.json',mode='w',encoding='utf8') as f:
    json.dump(diccionario,f)