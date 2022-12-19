#EJERCICIOS DE FUNCIONES

#1.Definir una función que reciba un poema (un string con formato de poema) y devuelva los versos del poema
# separados por el caracter "|":

'''ejemplo: Con diez cañones por banda
            viento en popa a toda vela
            no corta el mar, sino vuela
            un velero bergantín.

pasaría a ser: Con diez cañones por banda|viento en popa a toda vela|no corta el mar, sino vuela|un velero bergantín.'''

poema = "Con diez cañones por banda\nviento en popa a toda vela\nno corta el mar, sino vuela\nun velero bergantín."
def split_poema(poem,separator='|'):
    poem = poem.split('\n')
    return separator.join(poem)
print(split_poema(poema))

#2.Modificar la función del apartado anterior para que reciba un parámetro opcional llamado "line" que determina
#qué linea del poema queremos que devuelva la función (por ejemplo, si line es 2, la función devuelve la segunda 
# línea del poema). Si no pasamos ningún argumento, la función hará lo mismo que la del apartado anterior.
def split_poema2(poem,line=None,separator='|'):
    poem = poem.split('\n')
    if line:
        return poem[line-1]
    return separator.join(poem)
print(split_poema2(poema,2))
#otra forma:
def split_poema2(poem,line=None,separator='|'):
    if not line:
        return split_poema(poem)
    return poem.split('\n')[line-1]
print(split_poema2(poema,2))

#3.Definir una función que dibuje un gráfico horizontal de barras utilizando asteriscos para dibujar las barras.
#La función recibe como argumento un diccionario donde las claves son strings (por ejemplo, el nombre de distintos países)
#y los valores serán números enteros.
puntos_eurovision = {
    'Italia': 30,
    'España': 10,
    'Alemania':20,
    'Francia':2,
    'Australia':14}
'''
output:
Italia:         ******************************
España:         **********
Alemania:       ********************
Francia:        **
Australia:      **************
'''
def histograma(diccionario,drawing='*'):
    for k,v in diccionario.items():
        asteriscos = v*drawing
        print(k+':\t'+asteriscos)
histograma(puntos_eurovision)

#4.Definir una función que determine si un número es par o no. (La función devuelve un booleano)
# Por simplicidad asumimos que el usuario solo va a introducir números enteros.
def par(n):
    if n%2 == 0:
        return True
    else:
        return False
x = int(input('Introduce un número: '))
if par(x):
    print('Es par.')
else:
    print('Es impar.')

#5.Definir una función que sirva para determinar el mayor y el menor valor de una lista.
numbers = [1,2,3,4,5,6,7,8]
def mayor_menor(lista):
    a = max(lista)
    b = min(lista)
    return a,b
print('el mayor valor de la lista es '+str(mayor_menor(numbers)[0])+' y el menor es '+str(mayor_menor(numbers)[1]))

#6.Modificar la función del apartado anterior para que el usuario pueda introducir tantas listas como desee.
#ejemplo:
lista_1 = [1,2,3,4,5]
lista_2 = [3,4,5,6,7,8]
lista_3 = [-1,4,5]
#con estas tres listas la función devolverá: (8,-1)
def mayor_menor(*args):
    a = max(args)
    b = min(args)
    return a,b
print(mayor_menor(*lista_1,*lista_2,*lista_3))

#7.Definir una función que sirva para determinar si una palabra/string es capicúa o no. 
# (La función devuelve un booleano)
def capicua(word):
    for i in range(0,len(word)//2):
        if word[i] != word[-(i+1)]:
            return False
    return True
#otra forma:
def capicua2(word):
    for i in range(0,len(word)//2):
        if word[i] == word[-(i+1)]:
            continue
        return False
    return True

x = input('Introduce una palabra: ')
if capicua(x):
    print('Es capicua.')
else:
    print('No es capicua.')

#8.Definir una función que cuente las palabras de un texto (devuelve un número de palabras).
def cuenta_palabras(text):
     return len(text.split())

text = "hola buenas, que tal estas ?"
print(cuenta_palabras(text))

#9.Repetir el ejercicio anterior pero ahora, teniendo en cuenta que puede haber signos de puntuación 
# y que no queremos contarlos como palabras.
import string
def cuenta_palabras2(text):
    for c in text:
        if c in string.punctuation:
            text = text.replace(c," ")
    return cuenta_palabras(text)
print(cuenta_palabras2(text))

#10.Definir una función que pase de binario a decimal.
def bin_to_dec(num):
    num = str(num)
    potencia = len(num)-1
    resultado = 0
    for i in num:
        if i == '1':
            resultado += 2**potencia
        elif i == '0':
            pass
        else:
            return 'ERROR'
        potencia -= 1
    return resultado

print(bin_to_dec(input('binario: ')))

#11. Define una función que reciba un número y devuelva True si es primo y false si no lo es.


def es_primo(num):
    for i in range(2,num):
        if num%i==0:
            resultado = False
            break
        else:
            resultado = True
    return resultado



#12. Define una función que reciba una lista de números y devuelva un conjunto que incluya los números
#primos de dicha lista. Puedes utilzar la función que has definido en el ejercicio anterior.

def conjunto_primos(lista):
    conjunto = set()
    primo = False
    for e in lista:
        for i in range(2,e):
            if e%i==0:
                primo = False
                break
            else:
                primo = True
        if primo == True:
            conjunto.add(e)
    return conjunto




#13. Definir una función que reciba los siguientes parámetros:
#-tareas: Un diccionario cuyas claves son los nombres de distintas tareas y cuyos valores son el número de horas
#que se tarda en completar cada una.
#-jornada: El número de horas diarias que trabaja la persona.
#La función devuelve el número de días que tardaría la persona en completar todas las tareas.
trabajos = {'formulario':2,'presentación del proyecto':5,'limpieza de base de datos':20,'mantenimiendo de servidores':15}

import math

def obtener_dias(tareas:dict[str,int],jornada:int=8)->float:
    total:int=sum(tareas.values())
    return total/jornada


#14. Modificar la función anterior para que reciba un parámetro opcional 'tarea' cuyo valor por defecto
#sea None. Si tarea es None, la función actúa exactamente igual que en el ejercicio anterior. Si no,
#la función devuelve el número de días que tardaría en completar la tarea indicada.
#Ejemplo: jornada=3,tarea='formulario' -> devuelve: 1

def obtener_dias(tareas:dict[str,int],trabajo:str,jornada:int=8)->int:
    horas:int = trabajos.get(trabajo)
    horas = trabajos[trabajo]
    return math.ceil(horas/jornada)



#15. El diccionario 'datos' recoge información sobre las precipitaciones (mm^3) organizada por fecha y ciudad.
#Define una función que reciba como parámetros el nombre de una ciudad, un umbral de mm^3 y un diccionario con
#la misma estructura que el del ejemplo. La función devuelve una lista con todas las precipitaciones de
#dicha ciudad que superen el umbral. Si la ciudad no existe en el diccionario, la función devuelve None.

datos = {'Madrid':{
        '18-06-2021':4.2,
        '21-10-2021':5.2
        },
        'Valencia':{
        '18-06-2021':4.2,
        '21-10-2021':5.2}}

def get_dias_lluviosos(datos:dict[str,dict[str,float]],ciudad:str,umbral:float=0.0)->list:
    precipitaciones = []
    if ciudad not in datos:
        print('No hay datos disponibles.')
        return None
    for a in datos[ciudad]:
        if datos[ciudad][a] > umbral:
            precipitaciones.append(a)
    return precipitaciones

print(get_dias_lluviosos(datos,'Madrid'))