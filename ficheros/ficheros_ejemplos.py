#SIEMPRE SIEMPRE SIEMPRE que abrimos un fichero lo tenemos que CERRAR después
#Si abrimos un fichero con with, python hace el close() por nosotros :))

fichero = 'nombres.txt'  #qué tengo que poner como fichero?
            #qué pasa si no está en la misma carpeta?
            #qué pasa si el fichero no existe?

#leer un fichero
with open(fichero,mode='r',encoding='utf8') as f:
    print(f.read()) #Qué va a imprimir ?


#leer un fichero por lineas (con un bucle for)
with open(fichero,encoding='utf8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

#escribir nuevos nombres en el fichero (write o append?)

with open(fichero,mode='a',encoding='utf8') as f:
    f.write('\nPedro')


#leer por líneas el fichero nombres.txt y escribir su contenido en otro fichero nombres2.txt
with open(fichero,mode='r',encoding='utf8') as f:
    lines = f.readlines()

with open('nombres2.txt',mode='w',encoding='utf8') as f:
    for line in lines:
        f.write(line)






# y si quiero guardar objetos más complejos no solo strings ?
import pickle
lista = [1,2,3,4,5]

#guardar una LISTA en un fichero .pickle
with open('lista.pickle',mode='wb') as f:
    pickle.dump(lista,f)

#leer el fichero de la lista
with open('lista.pickle',mode='rb') as f:
    print(pickle.load(f))


#cambiar el primer valor de la lista por 9 y comprobar que hemos hecho el cambio

with open('lista.pickle',mode='rb') as f:
    lista = pickle.load(f)

lista[0]=9

with open('lista.pickle',mode='wb') as f:
    pickle.dump(lista,f)

with open('lista.pickle',mode='rb') as f:
    print(pickle.load(f))


'''
#¿Qué diferencia hay entre load y loads, y dump y dumps?
with open('lista.pickle',mode='rb') as f:
    y=pickle.load(f)
    x=pickle.loads(f)
'''

#¿OTROS TIPOS DE FICHERO? 









import csv #comma separated values
with open('personas.csv', mode='r',encoding='utf8') as fichero:
    csv_reader = csv.reader(fichero, delimiter=',')#guardamos las líneas del fichero en csv_reader
    contador = 0
    for linea in csv_reader: #¿qué es una línea en un csv?

        if contador == 0:
            cabeceras = linea
            contador += 1          
        else:
            print('Línea ' + str(contador) + ':')            
            for i in range(len(cabeceras)):
                print(cabeceras[i], '->', linea[i])
            contador += 1

#y para abrir en modo escritura ? cómo añado más personas al fichero ? y si hay un campo que no tengo?
with open('personas.csv', mode='a', encoding='utf8', newline='') as fichero:
    csv_writer = csv.writer(fichero, delimiter=',')
    linea = ['Pablo','Buendía','24']
    csv_writer.writerow(linea)
    linea = ['Enrique', None,'15']
    csv_writer.writerow(linea)



#escribir un diccionario como un csv
with open('test.csv', mode='w', encoding='utf8', newline='') as fichero:
    cabeceras = ['Nombre','Apellido','Email']
    csv_writer=csv.DictWriter(fichero, fieldnames=cabeceras, delimiter=',')
    csv_writer.writeheader()
    dict = {
    'Nombre': 'Pablo',
    'Apellido': 'Buendía',
    'Email': 'yo@miweb.com'
    }
    csv_writer.writerow(dict)










import json
#puedo guardar listas, diccionarios, etc y leerlos tal cual
#no puedo guardar objetos (para eso usamos pickle)

'''
diccionario = {
    'nombre':'Marta',
    'edad':25
}

#almacenar y cargar el diccionario
with open('ejemplo.json',mode='w',encoding='utf8') as f:
    json.dump(diccionario,f)
'''
with open('ejemplo.json',mode='r',encoding='utf8') as f:
    print(json.load(f))
